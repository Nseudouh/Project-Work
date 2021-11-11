import sqlite3
db = sqlite3.connect("users.db")
cursor = db.cursor()

sql = "SELECT * FROM users"
cursor.execute(sql)
print(input("Enter the numbers of records to be read"))
print("first 2 users in the system")
many_records = cursor.fetchmany(2)
for records in many_records:
    print(records)


db.close()



