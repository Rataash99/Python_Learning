# import sqlite3

# #connect to Database
# conn = sqlite3.connect('./Sqlite_Database_practice/customer.db')

# # create a cursor
# cursor = conn.cursor()

# # # create a table
# # cursor.execute("""CREATE TABLE customers (
# #         first_name text,
# #         last_name text,
# #         email text
# #     )""")

# # list of customers
# many_customers = [
#     ("Rahul", "Singh", "rahul.singh@gmail.com"),
#     ("Nitin", "kumar", "nitin.kumar@gmail.com"),
#     ("Simran", "Singh", "simran.singh@gmail.com")
# ]

# # inserting a single data row
# # cursor.execute("INSERT INTO customers VALUES ('Rohit', 'Singh', 'rohit.singh11299@gmail.com')")

# # inserting large data row
# # cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# #Query the Databae
# cursor.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'K%'")

# # fetching the first item of the table
# # cursor.fetchone()

# # fetching multiple items from the table
# # cursor.fetchmany()

# # fetching all items of table
# items = cursor.fetchall()

# print(f"S.No \t First_Name \t Last_Name \t Email")
# for item in items:
#     print(f"{item[0]} \t\t {item[1]} \t\t {item[2]} \t\t {item[3]}")

# # DATATYPE in sqlite
# # NULL
# # INTEGER
# # REAL
# # TEXT
# # BLOB

# # commit our command
# conn.commit()

# # close your connection
# conn.close()

import operations_CRUD as opc

url = "./Sqlite_Database_practice/customer.db"
db_name = "customers"
entities = [
    "first_name text",
    "last_name text",
    "email text"
]
# opc.create_table(url, db_name, entities)

# row_data = ("Rohit", "Singh", "rohit.singh11299@gmail.com")
# opc.insert_one(row_data, url, db_name)

data = [
    ("Rahul", "Singh", "rahul.singh349349@gmail.com"),
    ("Sarla", "Singh", "sarlarr@gmail.com"),
    ("Nitin", "Kumar", "nitin.kumar@gmail.com")
]
# opc.insert_many(data, url, db_name)

# entity = "first_name"
# change = "salman"
# rowid = 3

# opc.update_table(entity, change, rowid, url, db_name)

# opc.delete_records(url, db_name, 3)
# opc.delete_table(url, db_name)

opc.show_db_entries(url, db_name)