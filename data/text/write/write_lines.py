input("enter a file path")
file_path = "output.txt"
lines =["This is the first line.\n", "This is the second.\n", "This is the third line.\n"]
try:
    with open(file_path, "w")as file:
        file.writelines(lines)
        print("this data has been written to the file")

except IOError:
    print("this file cannot be read ")