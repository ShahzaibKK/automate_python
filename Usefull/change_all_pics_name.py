import os

folder_path = r"D:\Khuram Tiles\Main Files\Huamei Ceramics\HM\10x20"  # Replace with the path to your folder
prefix = "25HM"  # Define the desired prefix

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    file_ext = os.path.splitext(filename)[1]  # Get the file extension
    new_filename = f"{prefix}{filename}"

    # Rename the file
    os.rename(
        os.path.join(folder_path, filename), os.path.join(folder_path, new_filename)
    )
