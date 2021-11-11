import sqlite3
db = sqlite3.connect("users.db")
cursor = db.cursor()

sql = "SELECT * FROM users"
cursor.execute(sql)
all_records = cursor.fetchall()
for records in all_records:
    print(records)

db.close()
