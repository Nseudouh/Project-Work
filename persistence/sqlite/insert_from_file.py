import csv
import sqlite3
print("Please enter the file path")
file_path = input()

data = []
with open(file_path)as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        data.append(line)

print("Inserting data into the database.....")

db = sqlite3.connect("users.db")
cursor = db.cursor()

for record in data:
    sql = "INSERT INTO users (name, height, weight, date_of_birth) VALUES (?,?,?,?)"
    values = [record[0], record[1], record[2], record[3]]
    cursor.execute(sql, values)
db.commit()
db.close()
print(f"Done! {len(data)} records inserted")








