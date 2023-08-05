from pathlib import Path

same_path = Path()
print(list(same_path.glob("*.db")))

for text_file_path_obj in same_path.glob("*.db"):
    print(text_file_path_obj)

not_exists = Path("C:/Fucking")
file_path = Path(r"C:/Users\shahz\Desktop/num.txt")
e_drive = Path("E:/")
print(same_path.exists())
print(same_path.is_dir())
print(same_path.is_file())
print(not_exists.exists())
print(file_path.is_file())
print(e_drive.exists())
