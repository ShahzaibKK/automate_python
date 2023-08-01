import os
from pathlib import Path

p = Path(os.path.abspath("chapter9_file\\first.py"))
print(p.suffix)
print(os.path.getsize(p))
print(
    os.path.getsize(
        Path("D:\Khuram Tiles\Main Files\Huamei Ceramics/availble\compressed_images")
    )
)
print(
    os.listdir(
        Path("D:\Khuram Tiles\Main Files\Huamei Ceramics/availble\compressed_images")
    )
)
