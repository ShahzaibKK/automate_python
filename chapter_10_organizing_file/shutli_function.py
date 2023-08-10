import shutil, os
from pathlib import Path

p = Path("chapter_10_organizing_file")
# print(os.path.abspath(p))
p = os.chdir(os.path.abspath(p))
# os.makedirs("spam", exist_ok=True)
print(os.listdir(p))
# shutil.copytree(
#     "spam",
#     "spam2",
# )
# shutil.move("spam/test.txt", "spam2/new_test.txt")
pic_list = []
pic = Path("D:\Khuram Tiles\Main Files\Huamei Ceramics\\availble\compressed_images")
for picture in pic.glob("*.jpg"):
    os.unlink(picture)
    print(f"the fwolloing picture {picture} has been deleted!")
