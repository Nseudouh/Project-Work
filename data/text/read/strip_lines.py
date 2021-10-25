input("enter a file path")
file_path = "quotes.txt"
try:
    with open(file_path)as file:
        for line in file.readlines():
            print(line.strip())
except IOError:
    print("cannot be read")




