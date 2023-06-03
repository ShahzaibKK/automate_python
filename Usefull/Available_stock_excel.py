import shutil
import os
from openpyxl import load_workbook

source_folder = input("Please enter the full address of the source folder: ")
destination_folder = input("Please enter the full address of the destination folder: ")
excel_file = input("Please enter the full address of the Excel file: ")

# Load the workbook
workbook = load_workbook(excel_file)

# Select the active sheet
sheet = workbook.active

# Get the column containing the file names
column = sheet["A"]

# Iterate through the file names
for cell in column:
    if cell.value is not None:
        filename = str(cell.value).strip()

        source_path = os.path.join(source_folder, f"{filename}.jpg")
        destination_path = os.path.join(destination_folder, f"{filename}.jpg")

        # Copy the file from source to destination
        if os.path.exists(source_path):
            shutil.copy(source_path, destination_path)
            print(f"File copied: {filename}.jpg")
        else:
            print(f"File not found: {filename}.jpg")

# Save the modified workbook (optional)
# workbook.save(excel_file)
