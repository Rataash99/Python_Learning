import sqlite3

conn = sqlite3.connect("./Sqlite_Database_practice/customer.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE customers")

print(cursor.fetchall())

conn.commit()
conn.close()