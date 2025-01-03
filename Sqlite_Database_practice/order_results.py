import sqlite3

conn = sqlite3.connect("./Sqlite_Database_practice/customer.db")
cursor = conn.cursor()

cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
cursor.execute("SELECT rowid, * FROM customers ORDER BY first_name DESC")
items = cursor.fetchall()

print(f"S.No \t\tFirst Name \t\tLast Name \t\tEmail")
print("---\t\t\t-------\t\t\t------\t\t\t----------------------")
for item in items:
    print(f"{item[0]} \t\t\t{item[1]} \t\t\t{item[2]} \t\t\t{item[3]}")

conn.commit()
conn.close()