import sqlite3

# connect to Database
conn = sqlite3.connect("./Sqlite_Database_practice/customer.db")

# create a cursor
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
    )""")

# Query the database
cursor.execute("SELECT rowid, * FROM customers")

# fetching items of table
items = cursor.fetchall()

print(f"S.No \t\tFirst Name \t\tLast Name \t\tEmail")
print("---\t\t\t-------\t\t\t------\t\t\t----------------------")
for item in items:
    print(f"{item[0]} \t\t\t{item[1]} \t\t\t{item[2]} \t\t\t{item[3]}")

# commiting changes
conn.commit()

# closing the connection
conn.close()
