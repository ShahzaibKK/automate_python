import PyPDF2, os, openpyxl
from openpyxl.worksheet.worksheet import Worksheet
import pprint, shutil
from PIL import Image

with open("meetingminutes.pdf", "rb") as pdf_file_obj:
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    kk = pdf_reader.pages[1].extract_text()
    with open("Text_From_PDF.txt", "w") as pdf_text:
        pdf_text.write(kk)


wb = openpyxl.load_workbook(
    r"D:\Khuram Tiles\Main Files\Huamei Ceramics\available_stock.xlsx"
)
sheet: Worksheet = wb.active
print(sheet.title)
artices_set = set()
for data in range(sheet.min_row, sheet.max_row):
    artices = sheet["A" + str(data)].value
    if artices:
        artices_set.add(artices)
# pprint.pprint(artices_set)

os.makedirs("Kokala", exist_ok=True)
source_path = r"D:\Khuram Tiles\Main Files\Huamei Ceramics\MIX Pics"
for artile in artices_set:
    file_name_ = artile + ".jpg"
    articel_path = os.path.join(source_path, file_name_)
    if os.path.exists(articel_path):
        print(f"Yes {artile} is available")
        size = os.path.getsize(articel_path) / (1024**2)
        print(f" Size: {size:.2f} MB")
        shutil.copy(articel_path, os.path.join("./Kokala", file_name_))
        if size > 3:
            shutil.rmtree()
    else:
        print("not avaiable")
