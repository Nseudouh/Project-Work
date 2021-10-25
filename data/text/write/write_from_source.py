source_file_path = "quotes.txt"
destination_file_path = "output.txt"
lines = []
try:
    with open(source_file_path)as source_file_path:
        for line in source_file_path:
            lines.append(line.strip())
            print("the data has been displayed")

    with open (destination_file_path, "w")as destination_file_path:
        for line in lines:
            destination_file_path.write(f"\n{line}")
            print("this message has already been displayed")
except IOError:
    print("cannot read file")
