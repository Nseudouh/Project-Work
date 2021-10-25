input("enter file path")
file_path = "output.txt"
try:
    with open(file_path, "w") as file :
        file.write("data has been overwritten")
except IOError:
    print("cannot read file")