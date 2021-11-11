import sqlite3
db = sqlite3.connect("users.db")
cursor = db.cursor()

sql = "INSERT INTO users (name, height, weight ,date_of_birth) VALUES (?,?, ?, ?)"
new_records = "Max", 1.9, 90, "2020-02-02"
cursor.execute(sql, new_records)
print(input("Please enter the name of the user :"))

print(input("Please the enter the height m :"))

print(input("Please enter the weight kg :"))

print(input("Please enter the  date_of_birth: "))

print("The record has been added to the database")

print(cursor.lastrowid)

db.commit()

db.close()
