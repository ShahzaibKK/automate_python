import os

for folder_name, sub_folder, file_name in os.walk(
    os.path.abspath("chapter_10_organizing_file")
):
    print(f"The Curent Folder is {folder_name}")

    for sub_folderr in sub_folder:
        print(f"The Sub Folder of {folder_name}: {sub_folderr}")

    for file in file_name:
        print(f" File in Side {folder_name}: {file_name}")

    print("")
