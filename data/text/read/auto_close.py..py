file_path = "quotes.txt"
try:
    with open(file_path)as file:
        print(file.readlines())
except IOError:
    print("this file cannot be read")