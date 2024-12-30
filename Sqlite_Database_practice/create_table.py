import sqlite3

# connect to Database
conn = sqlite3.connect("./Sqlite_Database_practice/customers.db")

# create a cursor
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
    )""")

many_customers = [
    ("Rahul", "Singh", "rahul.singh@gmail.com"),
    ("Naman", "Kumar", "nitin.kumar@gmail.com"),
    ("Simran", "Singh", "simran.singh@gmail.com"),
    ("Raunak", "Singh", "rahul.singh@gmail.com"),
    ("Navjot", "Kumar", "nitin.kumar@gmail.com"),
    ("Rashid", "Ahmed", "simran.singh@gmail.com"),
    ("Noor", "Fatima", "rahul.singh@gmail.com"),
    ("Nikita", "Kandari", "nitin.kumar@gmail.com"),
    ("Sonal", "Chauhan", "simran.singh@gmail.com")
]
# Query the database
cursor.execute("SELECT rowid, * FROM customers")

# fetching items of table
items = cursor.fetchall()

print(f"S.No \t\tFirst Name \t\tLast Name \t\tEmail")
print("---\t\t\t-------\t\t\t------\t\t\t----------------------")
for item in items:
    print(f"{item[0]} \t\t\t{item[1]} \t\t\t{item[2]} \t\t\t{item[3]}")

conn.commit()
conn.close()
