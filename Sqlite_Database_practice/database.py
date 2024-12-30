import sqlite3

#connect to Database
conn = sqlite3.connect('./Sqlite_Database_practice/customer.db')

# create a cursor
cursor = conn.cursor()

# # create a table
# cursor.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
#     )""")

# list of customers
many_customers = [
    ("Rahul", "Singh", "rahul.singh@gmail.com"),
    ("Nitin", "kumar", "nitin.kumar@gmail.com"),
    ("Simran", "Singh", "simran.singh@gmail.com")
]

# inserting a single data row
# cursor.execute("INSERT INTO customers VALUES ('Rohit', 'Singh', 'rohit.singh11299@gmail.com')")

# inserting large data row
# cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

#Query the Databae
cursor.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'K%'")

# fetching the first item of the table
# cursor.fetchone()

# fetching multiple items from the table
# cursor.fetchmany()

# fetching all items of table
items = cursor.fetchall()

print(f"S.No \t First_Name \t Last_Name \t Email")
for item in items:
    print(f"{item[0]} \t\t {item[1]} \t\t {item[2]} \t\t {item[3]}")

# DATATYPE in sqlite
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# commit our command
conn.commit()

# close your connection
conn.close()

