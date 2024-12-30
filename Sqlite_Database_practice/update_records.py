import sqlite3

conn = sqlite3.connect("./Sqlite_Database_practice/customer.db")

cursor = conn.cursor()

# verifying the records
cursor.execute("SELECT * FROM customers WHERE last_name = 'kumar'")
print("Before updating :-\n", cursor.fetchall())


cursor.execute(""" UPDATE customers SET first_name = 'Naman' WHERE last_name = 'kumar' """)
cursor.execute(""" UPDATE customers SET first_name = 'Rashid' WHERE rowid = 7 """)
cursor.execute("""UPDATE customers SET first_name = 'Noor' WHERE rowid = 8 """)
cursor.execute(""" UPDATE customers SET first_name = 'Nikita' WHERE rowid = 9 """)
conn.commit()

cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()

print(f"S.No \t First_Name \t Last_Name \t Email")
for item in items:
    print(f"{item[0]} \t\t {item[1]} \t\t {item[2]} \t\t {item[3]}")
