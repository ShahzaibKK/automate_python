import time
import re
import sys
import platform
import datetime
import uuid
import hashlib
import shutil
from pathlib import Path
from configparser import ConfigParser
from PIL import Image as PIL_Image, ImageDraw, ImageFont
from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Image,
    Table,
    TableStyle,
    PageBreak,
    Paragraph,
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
import logging
import requests

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Stock PDF Generator

Author: Shahzaib KK +92 336 8311100

This Python script is designed to generate PDF documents from a collection of images. It is specifically tailored to the needs of Khuram Tiles, Peshawar, for creating product catalogs. The script compresses images, adds quantity information, and optionally includes a logo. It is intended to automate the process of generating these catalogs.

Usage:
- Ensure you have the required libraries installed (Pillow, openpyxl, reportlab, requests).
- Prepare your images and Excel file as per the specified format.
- Run this script with the desired options to generate the PDF.

Options:
- 'logo': Include the company logo in the PDF.

For more detailed information on how to use this script, please refer to the documentation or contact the author.

Note:
This script is part of an automation project and is customized for a specific use case. It may require adjustments for different scenarios.
"""

LICENSE_PATH = r"D:\KK's\automate_python\KINGs_work\Office_license.key"
CONFIG_PATH = r"D:\KK's\automate_python\KINGs_work\config.ini"
WATERMARK_TEXT = "KHURAM TILES PESHAWAR"


def verify_license():
    # Get the machine's MAC address
    mac_address = str(uuid.getnode())
    secret = "M_AMIR"

    # Hash the MAC address
    current_hashed_mac = hashlib.sha256((mac_address + secret).encode()).hexdigest()

    # Read the hashed MAC from the license file
    try:
        with open(LICENSE_PATH, "r") as license_file:
            stored_hashed_mac = license_file.read().strip()
    except FileNotFoundError:
        logging.error("Error: license.key not found.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error while reading license file: {e}")
        sys.exit(1)

    # Validate the hash
    if current_hashed_mac != stored_hashed_mac:
        logging.error("Error: License validation failed. Unauthorized machine.")
        sys.exit(1)

    logging.info("License validated successfully.")


if not Path(CONFIG_PATH).exists():
    logging.error("Config file not found. Please ensure the path is correct.")
    sys.exit(1)

config = ConfigParser()
try:
    config.read(CONFIG_PATH)
except Exception as e:
    logging.error(f"Unexpected error while reading config file: {e}")
    sys.exit(1)

# Check if the operating system is Windows
if platform.system() == "Windows":
    # Check if it's Windows 11
    if platform.version().startswith("10.0.2"):
        # Adjust the path for Windows 11
        desktop_path = Path(Path.home() / r"OneDrive\Desktop")
    else:
        # For other Windows versions
        desktop_path = Path.home() / "Desktop"

    ALL_RECORDS = desktop_path / "DATA"
    ALL_RECORDS.mkdir(exist_ok=True)

    COMPRESS_IMAGE_PATH = desktop_path / "DATA" / "compressed_images"
    COMPRESS_IMAGE_PATH.mkdir(exist_ok=True)

    try:
        all_pics = Path(config["Paths_bro"]["all_pics"])
        KT_LOGO = Path(config["Paths_bro"]["company_logo"])
    except KeyError as e:
        logging.error(f"Key '{e.args[0]}' is missing in config.ini.")
        sys.exit(1)
    destination_path_comp = COMPRESS_IMAGE_PATH
    formated_date = datetime.date.today().strftime("%d-%m-%Y")
    pdf_file = ALL_RECORDS / f"Available_Stock_{formated_date}.pdf"
    # show_first = input("which articels you want to show first, e.g: 36DM, 40CP, 36HM etc: ")
    MISSING_FILES = set()
    MISSING_FILES_PATH = ALL_RECORDS / "Missing_Images.txt"
    AVAILABLE_STOCK = desktop_path / "available_stock.xlsx"

else:
    print("This script is intended for Windows operating systems.")


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
time.sleep(2)


def collect_articels():
    """Load Excel File And Store the articels in a set"""
    wb = load_workbook(AVAILABLE_STOCK)
    if len(sys.argv) > 2:
        if sys.argv[2] == "DM":
            article_regex = re.compile(r"\d{2}DM\d{3}")
        else:
            article_regex = re.compile(r"(\w)?\d{2}\w{2}\d{3}")
    else:
        article_regex = re.compile(r"(\w)?\d{2}\w{2}\d{3}")

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
    return articels_name


def collect_qty():
    # Collect your article names using a more descriptive variable name
    article_names = collect_articels()

    # Load the Excel workbook
    wb = load_workbook(AVAILABLE_STOCK)
    sheet: Worksheet = wb.active

    # Initialize a dictionary to store article names and their quantities
    article_quantities = {}

    for article_name in article_names:
        article_regex = re.compile(rf"^{article_name}(\w+)?(\d+)?$")  # Adjusted regex

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
                                article_quantities[article_full_name] = (
                                    quantity_cell.value
                                )

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

    # Define your categories dictionary
    categories = {
        "36": "12x24 Glaze",
        "M36": "12x24 Matt",
        "40": "16x16 Glaze",
        "25": "10x20 Glaze",
        "M30": "12x12 Matt",
    }  # Add more categories as needed

    current_category = None
    category_lookup = {key: category for key, category in categories.items()}

    for image_path in image_paths:
        pure: str = image_path.stem[11:]
        article_regex_pattern = rf"^{pure}(\w+)?(\d+)?$"
        article_regex = re.compile(article_regex_pattern)

        # Check if the current article belongs to a new category
        category_text = category_lookup.get(pure[:2])
        if category_text and current_category != category_text:
            current_category = category_text
            # Add the category text to the elements
            if elements:
                elements.append(PageBreak())
            category_text = f"Category: {current_category}"

            # Create a Paragraph for the category text
            styles = getSampleStyleSheet()
            category_paragraph = Paragraph(category_text, styles["Heading2"])
            elements.append(category_paragraph)
            logging.info(f"Added new category: {current_category}")

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
                    ("FONTNAME", (0, 1), (-1, -1), "Helvetica-Bold"),
                    (
                        "FONTSIZE",
                        (0, 1),
                        (-1, -1),
                        13,
                    ),
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
        elements.extend(flowables)

    doc.build(elements)


def get_world_time():
    """Fetch current time from worldtimeapi.org."""
    try:
        curl = "http://worldtimeapi.org/api/timezone/Asia/Karachi"
        logging.debug(f"Fetching time from {curl}")
        res = requests.get(curl, timeout=10)
        res.raise_for_status()
        json = res.json()
        # Convert to offset-aware datetime
        return datetime.datetime.fromisoformat(json["datetime"])
    except (requests.RequestException, KeyError, ValueError) as e:
        logging.error(f"Error fetching time from worldtimeapi.org: {e}")
        return None


def get_timeapi_time():
    """Fetch current time using TimeAPI."""
    try:
        timeapi_url = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Karachi"
        logging.debug(f"Fetching time from {timeapi_url}")
        res = requests.get(timeapi_url, timeout=10)
        res.raise_for_status()
        json = res.json()
        # Convert to offset-aware datetime
        return datetime.datetime.fromisoformat(json["dateTime"])
    except (requests.RequestException, KeyError, ValueError) as e:
        logging.error(f"Error fetching time from TimeAPI: {e}")
        return None


def get_current_time():
    """Fetches the current time using APIs, with fallback to local time."""
    current_time = get_world_time()
    if not current_time:
        logging.error("worldtimeapi.org failed. Trying TimeAPI.")
        current_time = get_timeapi_time()
    if not current_time:
        logging.error("Both APIs failed. Falling back to local system time.")
        current_time = datetime.datetime.now(datetime.timezone.utc)  # Make offset-aware
    return current_time


def validate_license():
    """Validates the program license based on expiration date."""
    current_time = get_current_time()
    logging.debug(f"Current time: {current_time}")

    # Define license expiry date (offset-aware datetime)
    EXPIRE = datetime.datetime(2024, 12, 31, 23, 59, 59, tzinfo=datetime.timezone.utc)

    # Ensure comparison is valid
    if current_time.tzinfo is None:
        current_time = current_time.replace(tzinfo=datetime.timezone.utc)

    # Check license validity
    if EXPIRE < current_time:
        logging.error(
            "\n\n\n\n\n\n\tYour program license has expired. Please contact Shahzaib KK +92 336 8311100 to renew your license."
        )
        sys.exit()
    print("License is valid. Program continues...")


if __name__ == "__main__":
    # Call the function at the start of your script
    verify_license()
    validate_license()

    if len(sys.argv) > 1:
        if sys.argv[1] == "logo":
            watermark_text = WATERMARK_TEXT
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
            )
        else:
            logging.error(f"Not Availble: {article_path.stem}")
            MISSING_FILES.add(article_path)

    logging.info(f"\n\n\t Generating PDF Please Wait. . . . .")

    with open(MISSING_FILES_PATH, "w") as missing_report:
        missing_report.writelines(
            f"{missing_file.stem}\n" for missing_file in MISSING_FILES
        )

    if compress_images_path:
        if len(sys.argv) > 1:
            if sys.argv[1] == "logo":
                create_pdf(compress_images_path, str(pdf_file), KT_LOGO)
                watermark_text = WATERMARK_TEXT
            else:
                create_pdf(compress_images_path, str(pdf_file))
                watermark_text = ""

logging.info(f"\n\n\n\n\t ****PDF was Created****\n: {pdf_file}")
