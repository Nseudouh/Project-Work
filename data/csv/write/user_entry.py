import csv
file_path = "user_entries.csv"
try:
    with open(file_path, "w") as file:
        file.write("Year,Artist,Song Title")

year = int(input("please enter the year: "))
artist = input("please enter artist: ")
Song_title = input("please enter song title: ")
file.write("f\n{year}, {artist}, {Song_title}")

except IOError:
    print("cannot read file")


