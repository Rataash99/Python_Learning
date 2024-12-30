import sqlite3

conn = sqlite3.connect("./Sqlite_Database_practice/customers.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE customers ")

conn.commit()
conn.close()