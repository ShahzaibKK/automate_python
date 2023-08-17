import os, re
from pathlib import Path

# ! python 3
# a filling file name geps Project by Shahzaib kk


"""First i make 10 file using this Script like a pro"""
p = Path("D:\Spam_folder")
number = 0
if len(os.listdir(p)) < 1:
    while len(os.listdir(p)) < 10:
        Path.write_text(p / f"spam_0{number}.txt", "")
        number += 1
name_regex = re.compile(r"(spam_0)(\d)(\.txt)")
file_number = []
for file in os.listdir(p):
    mo = name_regex.search(file)
    file_number.append(int(mo.group(2)))
    print(mo.group(1))

print(file_number)

mini_number = min(file_number)
max_number = max(file_number)
miss_number = set(range(mini_number, max_number + 1)) - set(file_number)
print(f"Missing Number: {miss_number}")

for missing_num in miss_number:
    Path.write_text(p / f"{mo.group(1)}{missing_num}{mo.group(3)}", "")

for file in os.listdir(p):
    mo = name_regex.search(file)
    print(mo.group(1))
