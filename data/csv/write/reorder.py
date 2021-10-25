import csv
#creating a variable name
file_path = "../songs.csv."
dest_file_path = "output.csv"
#opened a song.csv file and a dest.csv file
try:
    with open(file_path)as file:
        with open(dest_file_path, "w") as dest_file:
            csv_reader = csv.reader(file) #created a csv reader for the sonngs.csv file
            headings = next(csv_reader) #read in and store the songs.csv as a headings
            for values in csv_reader: # for values in file: #used a loop to read the value of song.csv and wrote them to output
                file.write(f"\n{values[0]}, {values[1]}, {values[2]}, {values[3]}")

except IOError:
    print("cannot read file")