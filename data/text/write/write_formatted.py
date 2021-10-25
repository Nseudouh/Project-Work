file_path = input("enter file path")
file_path = "output.txt"
lines = ["This is the first line.", "This is the second.", "This is the third line."]
try:
    with open(file_path, "w")as file:
        for lines in lines:
            file.write(f"\n{lines}" )
            print("the data has been written to the file")

except IOError:
    print("cannot read file")
