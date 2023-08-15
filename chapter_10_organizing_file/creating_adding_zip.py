import zipfile
from pathlib import Path

with zipfile.ZipFile(Path.home() / "Downloads\pdftoimage (10).zip", "w") as new_zip:
    new_zip.write("wrong_txt.txt", compress_type=zipfile.ZIP_DEFLATED)
