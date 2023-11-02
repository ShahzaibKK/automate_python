import re, sys
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
import shutil
from PIL import Image as PIL_Image
from PIL import ImageDraw, ImageFont
from pathlib import Path
import logging
from reportlab.lib.pagesizes import letter
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
from reportlab.lib.units import inch
import datetime, time

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Stock PDF Generator

Author: Shahzaib KK +92 336 8311100

This Python script is designed to generate PDF documents from a collection of images. It is specifically tailored to the needs of Khuram Tiles, Peshawar, for creating product catalogs. The script compresses images, adds quantity information, and optionally includes a logo. It is intended to automate the process of generating these catalogs.

Usage:
- Ensure you have the required libraries installed (Pillow, openpyxl, reportlab).
- Prepare your images and Excel file as per the specified format.
- Run this script with the desired options to generate the PDF.

Options:
- 'logo': Include the company logo in the PDF.

For more detailed information on how to use this script, please refer to the documentation or contact the author.

Note:
This script is part of an automation project and is customized for a specific use case. It may require adjustments for different scenarios.
"""

ALL_RECORDS = Path.home() / "Desktop/DATA"
if not ALL_RECORDS.exists():
    ALL_RECORDS.mkdir()
COMPRESS_IMAGE_PATH = Path.home() / "Desktop/DATA/compressed_images"
if not COMPRESS_IMAGE_PATH.exists():
    COMPRESS_IMAGE_PATH.mkdir()

all_pics = Path(r"D:\Khuram Tiles\Main Files\Huamei Ceramics\MIX Pics")
destination_path_comp = COMPRESS_IMAGE_PATH
KT_LOGO = r"D:\Khuram Tiles\Main Files\Huamei Ceramics\MIX Pics\1.jpg"
formated_date = datetime.date.today().strftime("%d-%m-%Y")
pdf_file = ALL_RECORDS / f"Available_Stock_{formated_date}.pdf"
# show_first = input("which articels you want to show first, e.g: 36DM, 40CP, 36HM etc: ")
MISSING_FILES = set()
MISSING_FILES_PATH = ALL_RECORDS / "Missing_Images.txt"
AVAILABLE_STOCK = Path.home() / "Desktop/available_stock.xlsx"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# define custom sorting function
def custom_sorting(name: str):
    if name.startswith(name):
        return (0, name)
    else:
        return (1, name)


print("***** Create by Shahzaib KK +92 336 8311100 *****")
time.sleep(3)


def collect_articels():
    """Load Excel File And Store the articels in a set"""
    wb = openpyxl.load_workbook(AVAILABLE_STOCK)
    if len(sys.argv) > 2:
        if sys.argv[2] == "DM":
            article_regex = re.compile(r"\d{2}DM\d{3}")
        else:
            article_regex = re.compile(r"\d{2}\w{2}\d{3}")
    else:
        article_regex = re.compile(r"\d{2}\w{2}\d{3}")

    # Select the worksheet you want to read
    sheet: Worksheet = wb.active  # You can also select a specific sheet by name

    # Find the last row and column with data
    max_row = sheet.max_row
    max_col = sheet.max_column

    # Iterate through rows and columns to read the data
    articels_name = set()
    for row in range(1, max_row + 1):
        for col in range(1, max_col + 1):
            cell_value = sheet.cell(row=row, column=col).value
            if cell_value:
                mo = article_regex.search(str(cell_value))
                if mo:
                    articels_name.add(mo.group())

    # sorted_articles = sorted(articels_name, key=custom_sorting)
    return articels_name
    wb.close()


def collect_qty():
    # Collect your article names using a more descriptive variable name
    article_names = collect_articels()

    # Load the Excel workbook
    wb = openpyxl.load_workbook(AVAILABLE_STOCK)
    sheet: Worksheet = wb.active

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

    return article_quantities
    # Close the workbook
    wb.close()


def check_compressed_files(path_and_name: Path):
    if Path(path_and_name).exists():
        return True


def compress_images(
    image_path,
    destination_path,
    greater_than=0,
    remove_white_bg=True,
    target_resolution=(1800, 1800),
):
    size_MB = Path(image_path).stat().st_size / (1024 * 1024)
    file_name = Path(image_path).name
    compressed_file_name_dest = destination_path / f"compressed_{file_name}"

    if not check_compressed_files(compressed_file_name_dest):
        if size_MB > greater_than:
            image = PIL_Image.open(image_path)
            image = image.convert("RGB")

            # Resize the image to the target resolution
            image.thumbnail(target_resolution)

            # Add a watermark to the image
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("arial.ttf", 45)

            # Calculate the bounding box of the watermark text
            text_bounding_box = font.getbbox(watermark_text)

            # Calculate the position of the text in the bottom right corner
            image_width, image_height = image.size
            text_width, text_height = (
                text_bounding_box[2] - text_bounding_box[0],
                text_bounding_box[3] - text_bounding_box[1],
            )
            text_position = (
                image_width - text_width - 15,
                image_height - text_height - 35,
            )

            # Draw the text at the calculated position
            # Set the anchor argument to 'la'
            draw.text(
                text_position,
                watermark_text,
                font=font,
                fill=(234, 215, 139, 128),
                anchor="la",
            )

            image.save(compressed_file_name_dest, format="JPEG", quality=60)
            logging.info(f"Compressed {file_name} to {compressed_file_name_dest}")
        else:
            shutil.copy(image_path, destination_path)
            logging.info(f"Copied {file_name} to {destination_path}")
    else:
        logging.info(f"{file_name} already Compressed")

    return compressed_file_name_dest


def create_pdf(image_paths: Path, output_pdf_path, logo_path=None):
    folder = image_paths.parent
    qty = collect_qty()
    # Sort the image files to prioritize "36DM" images
    image_paths: Path = sorted(
        folder.glob("*"), key=lambda path: not path.name.startswith("compressed_36DM")
    )

    doc = SimpleDocTemplate(output_pdf_path, pagesize=letter)
    doc.background = colors.black
    elements = []

    if logo_path:
        logo = Image(logo_path, width=7 * inch, height=8 * inch)
        elements.append(logo)

    for image_path in image_paths:
        pure = image_path.stem[11:]
        article_regex = re.compile(rf"{pure}(\w+)?(\d+)?")

        # Create a list of flowables for this image and its corresponding table
        flowables = []

        # Add the image to the flowables
        image = Image(image_path, width=5.4 * inch, height=7.5 * inch)
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
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    (
                        "FONTSIZE",
                        (0, 0),
                        (-1, 0),
                        13,
                    ),
                    ("FONTNAME", (0, 1), (-1, -1), "Helvetica-Bold"),  # Add this line
                    (
                        "FONTSIZE",
                        (0, 1),
                        (-1, -1),
                        13,
                    ),  # Add this line to increase font size
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
                    ("TOPPADDING", (0, 1), (-1, -1), 3),
                    ("BOTTOMPADDING", (0, 1), (-1, -1), 3),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                    ("TEXTCOLOR", (0, 1), (-1, -1), colors.blue),
                    ("GRID", (0, 0), (-1, -1), 1.2, colors.black),
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
        # Set the background color of the page template
        page_template.background = colors.black

        # Add a page break before each new image and its table
        if elements:
            elements.append(PageBreak())

        elements.extend(flowables)

    doc.build(elements)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "logo":
            watermark_text = "KHURAM TILES PESHAWAR"
        else:
            watermark_text = ""

    compress_images_path = None
    for article in collect_articels():
        file_name_ = article + ".jpg"
        article_path = Path.joinpath(all_pics, file_name_)

        if Path(article_path).is_file():
            compress_images_path = compress_images(
                article_path,
                destination_path_comp,
                greater_than=0,
                remove_white_bg=True,
            )
        else:
            logging.error(f"Not Availble: {article_path.stem}")
            MISSING_FILES.add(article_path)

    with open(MISSING_FILES_PATH, "w") as missing_report:
        for missing_file in MISSING_FILES:
            missing_report.write(missing_file.stem + "\n")
    if compress_images_path:
        if len(sys.argv) > 1:
            if sys.argv[1] == "logo":
                create_pdf(compress_images_path, str(pdf_file), KT_LOGO)
                watermark_text = "KHURAM TILES PESHAWAR"
            else:
                create_pdf(compress_images_path, str(pdf_file))
                watermark_text = ""
logging.info(f"PDF was Created: {pdf_file}")
