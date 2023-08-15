import shutil, os
from pathlib import Path

# python 3
# selective Copying tool by Shahzaib Kk

current_path = Path()


def selective_copy(source_folder, destinatio_folder, file_ext):
    source_folder = os.path.abspath(source_folder)
    destinatio_folder = os.path.abspath(destinatio_folder)

    if not os.path.exists(destinatio_folder):
        os.makedirs(destinatio_folder)

    for fols, sub_fols, files in os.walk(source_folder):
        for file in files:
            if file.endswith(file_ext):
                source_path = os.path.join(fols, file)
                des_path = os.path.join(destinatio_folder, file)
                shutil.copy2(source_path, des_path)
                print(f"Copied! {file}")


destination = Path("./Selective_Copies")
file_ext = ".txt"

selective_copy(current_path, destination, file_ext)
