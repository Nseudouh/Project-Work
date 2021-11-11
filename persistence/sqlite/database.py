import sqlite3

print("database exercise")

db = sqlite3.connect("users.db")

cursor = db.cursor()

sql = """

INSERT INTO users (name, height, weight, date_of_birth) VALUES ("bob", 1.6, 80, "2020-01-01");

"""
cursor.execute(sql)
db.commit()
db.close()