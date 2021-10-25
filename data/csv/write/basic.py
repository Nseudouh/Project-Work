import csv
file_path = "sample.csv"
try:
    with open(file_path, "w")as file:
        file.write("f\nSample Song,Sample Artist,Sample Category,Sample Year")
except IOError:
    print("cannot read file")

