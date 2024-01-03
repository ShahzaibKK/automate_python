from pathlib import Path

path_file = Path(r"C:\Users\shahz\Downloads\12x24 HM Glaze.pdf")
num = 1
prefix = "36HM0"
for file_name in path_file.iterdir():
    new_name = file_name.joinpath(f"{prefix}{num}.jpg")
    file_name.rename(new_name)
    num += 1
    print(file_name)
