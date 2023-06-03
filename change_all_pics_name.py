import os

folder_path = "D:\Khuram Tiles\Main Files\Huamei Ceramics/apolo"  # Replace with the path to your folder
prefix = "36AP"  # Define the desired prefix

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    file_ext = os.path.splitext(filename)[1]  # Get the file extension
    new_filename = f"{prefix}{filename[2:]}"  # Create the new filename by replacing the first two characters

    # Rename the file
    os.rename(
        os.path.join(folder_path, filename), os.path.join(folder_path, new_filename)
    )
