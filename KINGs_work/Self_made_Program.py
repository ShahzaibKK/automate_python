import os, re, sys
import openpyxl
import shutil
from PIL import Image as PIL_Image
from pathlib import Path
import logging
from openpyxl.worksheet.worksheet import Worksheet
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from PIL import Image, ImageOps
import pprint
from reportlab.platypus import (
    SimpleDocTemplate,
    Image,
    Table,
    TableStyle,
    PageBreak,
    PageTemplate,
    Frame,
)
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus.flowables import Flowable
from reportlab.platypus import Spacer
from reportlab.lib import pagesizes
from reportlab.lib.units import inch


all_pics = r"D:\Khuram Tiles\Main Files\Huamei Ceramics\DM"
destination_path_comp = Path(r"D:\KK's\automate_python\Kokala")
KT_LOGO = r"D:\Khuram Tiles\Main Files\Huamei Ceramics\MIX Pics\1.jpg"
pdf_file = Path(r"C:\Users\shahz\Desktop\bro.pdf")
show_first = input("which articels you want to show first, e.g: 36DM, 40CP, 36HM etc: ")
logging.basicConfig(
    filename="mylog.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)


def collect_articels():
    """Load Excel File And Store the articels in a set"""
    wb = openpyxl.load_workbook(
        r"D:\Khuram Tiles\Main Files\Huamei Ceramics\available_stock.xlsx"
    )
    artile_regex = re.compile(r"\d{2}\w{2}\d{3}")

    # Select the worksheet you want to read
    sheet = wb["Table 1"]  # You can also select a specific sheet by name

    # Find the last row and column with data
    max_row = sheet.max_row
    max_col = sheet.max_column

    # Iterate through rows and columns to read the data
    articels_name = set()
    for row in range(1, max_row + 1):
        for col in range(1, max_col + 1):
            cell_value = sheet.cell(row=row, column=col).value
            if cell_value:
                mo = artile_regex.search(str(cell_value))
                if mo:
                    articels_name.add(mo.group())

    # define custom sorting function
    def custom_sorting(name: str):
        if name.startswith(show_first):
            return (0, name)
        else:
            return (1, name)

    sorted_articles = sorted(articels_name, key=custom_sorting)
    return sorted_articles
    wb.close()


def collect_qty():
    # Collect your article names using a more descriptive variable name
    article_names = collect_articels()

    # Load the Excel workbook
    wb = openpyxl.load_workbook(
        r"D:\Khuram Tiles\Main Files\Huamei Ceramics\available_stock.xlsx"
    )
    sheet = wb["Table 1"]

    # Initialize a dictionary to store article names and their quantities
    article_quantities = {}

    for article_name in article_names:
        article_regex = re.compile(rf"{article_name}(\w+)?(\d+)?")  # Adjusted regex

        for row in sheet.iter_rows():
            for i, cell in enumerate(row):
                if cell.value:
                    mo = article_regex.search(str(cell.value))
                    if mo:
                        article_full_name = mo.group(0)  # Get the complete article name
                        # Ensure the current cell is not the last in the row
                        if i < len(row) - 1:
                            quantity_cell = row[i + 1]
                            if quantity_cell.value:
                                article_quantities[
                                    article_full_name
                                ] = quantity_cell.value

    # Print the article names and their quantities
    # pprint.pprint(article_quantities)
    return article_quantities
    # Close the workbook
    wb.close()


def check_compressed_files(path_and_name):
    if Path(path_and_name).exists():
        return True


def compress_images(image_path, destination_path, greater_than=0, remove_white_bg=True):
    size_MB = Path(image_path).stat().st_size / (1024 * 1024)
    file_name = Path(image_path).name
    compressed_file_name_dest = destination_path / f"compressed_{file_name}"

    if not check_compressed_files(compressed_file_name_dest):
        if size_MB > greater_than:
            image = PIL_Image.open(image_path)
            image = image.convert("RGB")

            image.thumbnail((2500, 2500))
            image.save(
                compressed_file_name_dest, format="JPEG", quality=70
            )  # Use PNG format for transparency
            logging.info(f"Compressed {file_name} to {compressed_file_name_dest}")
        else:
            shutil.copy(image_path, destination_path)
            logging.info(f"Copied {file_name} to {destination_path}")
    else:
        logging.info(f"{file_name} already Compressed")

    return compressed_file_name_dest


def create_pdf(image_paths: Path, output_pdf_path, logo_path=None):
    logging.info(f"{image_paths}")
    kokala = image_paths.parent
    qty = collect_qty()

    doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
    elements = []

    if logo_path:
        logo = Image(logo_path, width=10 * inch, height=7 * inch)
        elements.append(logo)

    for image_path in kokala.glob("*"):
        pure = image_path.stem[11:]
        article_regex = re.compile(rf"{pure}(\w+)?(\d+)?")

        # Create a list of flowables for this image and its corresponding table
        flowables = []

        # Add the image to the flowables
        image = Image(
            image_path, width=20.5 * inch, height=7.3 * inch, kind="proportional"
        )

        flowables.append(image)

        # Create a data list for the table
        data = [["Article", "Quantity"]]
        for key in qty:
            mo = article_regex.search(key)
            if mo:
                article = key
                quantity = str(qty[mo.group()])
                data.append([article, quantity])

        # Create the table and set its style
        table = Table(data)
        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                    ("ALIGN", (0, 0), (-1, -1), "RIGHT"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                    ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ]
            )
        )
        flowables.append(table)

        # Create a frame for the flowables
        frame = Frame(
            doc.leftMargin,
            doc.bottomMargin,
            doc.width,
            doc.height,
            id=f"frame_{pure}",
        )

        # Create a PageTemplate for this frame
        page_template = PageTemplate(
            id=f"page_{pure}",
            frames=[frame],
        )

        # Add a page break before each new image and its table
        if elements:
            elements.append(PageBreak())

        elements.extend(flowables)

    doc.build(elements)


if __name__ == "__main__":
    for article in collect_articels():
        file_name_ = article + ".jpg"
        article_path = os.path.join(all_pics, file_name_)

        if Path(article_path).is_file():
            compress_images_path = compress_images(
                article_path, destination_path_comp, greater_than=1
            )

    # Modify this line to convert pdf_file to a string
    if len(sys.argv) > 1:
        if sys.argv[1] == "logo":
            create_pdf(compress_images_path, str(pdf_file), KT_LOGO)
        else:
            create_pdf(compress_images_path, str(pdf_file))
# create_pdf(compress_images_path, str(pdf_file), str(KT_LOGO))
