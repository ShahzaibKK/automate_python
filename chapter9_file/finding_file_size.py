import os
from pathlib import Path

p = Path(os.path.abspath("chapter9_file\\first.py"))
print(p.suffix)
print(os.path.getsize(p))
print(
    os.path.getsize(
        "D:\Khuram Tiles\Main Files\Huamei Ceramics/availble\compressed_images\compressed_1.jpg"
    )
)

print(
    os.listdir(
        Path("D:\Khuram Tiles\Main Files\Huamei Ceramics/availble\compressed_images")
    )
)
# let's check the total size of my Mix Pics Folder
total_size = 0
for filename in os.listdir("D:\Khuram Tiles\Main Files\Huamei Ceramics\MIX Pics"):
    total_size = total_size + os.path.getsize(
        os.path.join("D:\Khuram Tiles\Main Files\Huamei Ceramics\MIX Pics", filename)
    )
print(total_size)
