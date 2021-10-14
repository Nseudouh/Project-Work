import csv

file_path = "titanic.csv"

records = []

print("loading data ...", end="")

try:
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)

        for values in csv_reader:
            records.append(values)

    print("Done")
    print(f"Successfully loaded {len(records)} records")

except IOError:
    print("error")

