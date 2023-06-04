import os

folder_path = "D:\\Khuram Tiles\\Main Files\\Huamei Ceramics\\apolo"  # Replace with the path to your folder

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    file_ext = os.path.splitext(filename)[1]  # Get the file extension

    if filename.startswith("36APAP"):
        new_filename = "36AP" + filename[6:]

        # Rename the file
        os.rename(
            os.path.join(folder_path, filename), os.path.join(folder_path, new_filename)
        )
