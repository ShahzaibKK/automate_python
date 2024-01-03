import os

folder_path = (
    r"C:\Users\shahz\Downloads\16x16 HM.pdf"  # Replace with the path to your folder
)
prefix = "40HM0"  # Define the desired prefix

# Iterate through the files in the folder
num = 1
for filename in os.listdir(folder_path):
    file_ext = os.path.splitext(filename)[1]  # Get the file extension
    if num < 10:
        new_filename = f"{prefix}0{num}.jpg"
    else:
        new_filename = f"{prefix}{num}.jpg"

    # Rename the file
    os.rename(
        os.path.join(folder_path, filename), os.path.join(folder_path, new_filename)
    )
    num += 1
