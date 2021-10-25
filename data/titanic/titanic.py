import csv
file_path = "titanic.csv"
records = []
print("loading data...", end="")
try:
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)

        for value in csv_reader:
            records.append(value)
            print("Done!")
            print(f"Successfully downloaded {len(records)}records")

            print("""
              Please select one of the following options:
                
                [1] Display the names of all passenger
                [2] Display the number of passengers that survived
                [3] Display the number of passengers per gender
                [4] Display the number of passengers per age group
                
                """)
            selected_option = int(input())
            print(f"You have selected the option : {selected_option}")






except IOError:
    print("cannot read file ")


