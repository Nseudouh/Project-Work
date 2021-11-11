import sqlite3
db = sqlite3.connect("users.db")
cursor = db.cursor()
#input("Please enter user Id")
#OR
print("Please enter user Id")
int(input())
sql = "SELECT * FROM users WHERE VALUE = ?"
value = 1
cursor.execute(sql,value)
record = cursor.fetchone()
db.commit()
for records in record:
    print("Current users name are as follows;\n")
    print(f"Id: {record[0]}, height(kg): {record[1]}, weight; {record[2]}, date_of_birth; {record[3]}")













