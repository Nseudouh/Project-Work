file_path = "quotes.txt"
try:
    with open(file_path) as file:
        print(file.read())
except IOError:
    print("cannot read file")
    