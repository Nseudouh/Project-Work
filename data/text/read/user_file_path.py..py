input("enter a file_path")
file_path = "quotes.txt"
try:
    with open(file_path)as file:
        print(file.readlines())
except IOError:
    print("file cannot be read")



