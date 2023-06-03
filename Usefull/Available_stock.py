import shutil
import os

# source_folder = "D:\Khuram Tiles\Main Files\Huamei Ceramics\HM_12x24\HM 12x24_compressed"
# destination_folder = "D:\Khuram Tiles\Main Files\Huamei Ceramics\HM_12x24\HM 12x24_compressed\Today_available"
# file_list_file = "available_code.txt"

source_folder = input("Please Enter The full address of Source Folder: ")
destination_folder = input("Please Enter The full address Destination Folder: ")
file_list_file = input("Please Enter The full address of file that contain code: ")

# Read file names from the text file
with open(file_list_file, "r") as file:
    file_list = [line.strip() for line in file]

# Iterate through the file list
for filename in file_list:
    source_path = os.path.join(source_folder, f"{filename}.jpg")
    destination_path = os.path.join(destination_folder, f"{filename}.jpg")

    # Copy the file from source to destination
    try:
        shutil.copy(source_path, destination_path)
    except FileNotFoundError:
        print(f"File not found: {source_path}. Skipping...")
        continue
