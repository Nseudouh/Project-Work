import csv

file_path = "..//songs.csv"
try:
    with open(file_path)as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(headings)
except IOError:
    print("cannot read file")
