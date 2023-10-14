import csv, pprint

exmaple_csv = open("example.csv")
example_reader = csv.reader(exmaple_csv)
pprint.pprint(list(example_reader))
