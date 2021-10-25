import csv
file_path = "sample.csv"
try:
    with open(file_path, "a")as file:
        file.write("My Song,Unknown Artist,pop,2021")
except IOError:
    print("cannot read file")