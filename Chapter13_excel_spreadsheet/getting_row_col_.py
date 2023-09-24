import openpyxl

wb = openpyxl.load_workbook("../example.xlsx")
sheet = wb["Sheet1"]
print(tuple(sheet["A1":"C3"]))
print()
for rowOfCellObjects in sheet["A1":"C3"]:
    for cellObjects in rowOfCellObjects:
        print(cellObjects.coordinate,cellObjects.value)
    print("----END of Line----")

print()

print(list(sheet.columns)[1])

for cello in list(sheet.columns)[1]:
    print(cello.value)
