#! python3
# Project_remove_first_row.py - Removes the header from all CSV file in the
# current Working directory

from pathlib import Path
import csv

header_removed = Path.home() / "Desktop/Removed_Headers"
header_removed.mkdir(exist_ok=True)
csv_files_path = Path(
    r"C:\Users\shahz\Downloads\automate_online-materials\removeCsvHeader"
)
for csv_file in csv_files_path.glob("*.csv"):
    print(f"Removing Header From {csv_file} ...")

    csv_file_list = []
    with open(csv_file, "r") as csv_obj:
        reader_obj = csv.reader(csv_obj)
        for row in reader_obj:
            if reader_obj.line_num == 1:
                continue  # skiping first line
            csv_file_list.append(row)
        # write new csv file
    with open(header_removed / csv_file.name, "w", newline="") as csv_file_obj:
        write_obj = csv.writer(csv_file_obj)
        for row in csv_file_list:
            write_obj.writerow(row)
