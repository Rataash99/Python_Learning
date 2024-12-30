import sqlite3

#connect to Database
conn = sqlite3.connect('./Sqlite_Database_practice/customer.db')

# create a cursor
cursor = conn.Cursor()

cursor.execute("INSERT INTO customers VALUES ('Rohit', 'Singh', 'rohit.singh11299@gmail.com')")

# create a table
# cursor.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text,
#     )""")

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

