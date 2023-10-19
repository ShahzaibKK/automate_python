import csv


with open('exampleWithHeader.csv') as example_file:
    example_data = csv.DictReader(example_file)
    for row in example_data:
        print(f"{row["Timestamp"]}  {row["Fruit"]}  {row["Quantity"]}")
