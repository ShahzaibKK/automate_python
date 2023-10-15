import csv, pprint

exmaple_csv = open("example.csv")
example_reader = csv.reader(exmaple_csv)
# example_data = list(example_reader)
# pprint.pprint(example_data)
# pprint.pprint(example_data[3][1])

for row in example_reader:
    print(f"Row #{str(example_reader.line_num)} {str(row)}")
