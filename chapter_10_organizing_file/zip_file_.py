import zipfile, os
from pathlib import Path

p = Path(Path.home() / "Downloads\pdftoimage (10).zip")
check_init = zipfile.ZipFile(p)
# print(check_init.namelist())
# print(p)
ledger = check_init.getinfo("Apolo new 1/Ledger.pdf")
sr = 0
# for i in check_init.namelist():
#     sr += 1
#     print(f"{sr}: {i}")

print(f"Size of leder {ledger.file_size}")

print(ledger.compress_size)

print(f"Compressed file is {round(ledger.file_size / ledger.compress_size,2)}x smaller")
# check_init.extract("Apolo new 1/Ledger.pdf")
check_init.close()
