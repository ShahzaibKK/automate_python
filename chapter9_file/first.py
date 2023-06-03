import os
from pathlib import Path

my_path = Path("D:/") / "KK's"
print(my_path)
print(Path.cwd())
os.chdir(my_path)
print(Path.cwd())
print(os.getcwd())
print(Path.home())
os.makedirs(
    "creting/first/python/folder", exist_ok=True
)  # make one or more sub-directory
print(os.getcwd())
Path("creting/first/").mkdir()  # only make one directory
