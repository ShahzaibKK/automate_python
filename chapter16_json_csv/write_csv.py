import csv

with open("write.csv", "w", newline="") as write_csv:
    output_data = csv.writer(write_csv)
    output_data.writerow(["spam", "becon", "ham"])
    output_data.writerow(["Hello, World!", "becon", "ham"])
    output_data.writerow(["spam", "becon", "ham"])

with open("write2.tsv", "w", newline="") as write_csv:
    output_data = csv.writer(write_csv, delimiter="\t", lineterminator="\n\n")
    output_data.writerow(["spam", "becon", "ham"])
    output_data.writerow(["Hello, World!", "becon", "ham"])
    output_data.writerow(["spam", "becon", "ham"])
