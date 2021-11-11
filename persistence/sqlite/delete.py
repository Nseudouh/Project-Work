import sqlite3
db = sqlite3.connect("users.db")
cursor = db.cursor()
values = input("Enter a users Id")

sql = "SELECT * FROM users WHERE id = 10"

cursor.execute(sql)
record = cursor.fetchone()
print("The record has been found")
for records in record:
    print(f"id; {record[0]}, height: {record[1]}, weight : {record[2]}, date of birth {record[3]}")


sql = "DELETE FROM users WHERE Id = ?"
value = [1]
cursor.execute(sql, value)
db.commit()
print("The recorded has been deleted")



