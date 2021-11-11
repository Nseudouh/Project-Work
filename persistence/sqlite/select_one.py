import sqlite3

db = sqlite3.connect("users.db")
cursor = db.cursor()

sql = "SELECT * FROM users"
cursor.execute(sql)

single_records = cursor.fetchone()

for record in single_records:
    print(record)

db.close()