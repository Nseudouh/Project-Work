import csv
file_path = "../songs.csv"
try:
    with open(file_path)as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"{headings}\n")

        for values in csv_reader:
            print(values[0])
except IOError:
    print("cannot read file")