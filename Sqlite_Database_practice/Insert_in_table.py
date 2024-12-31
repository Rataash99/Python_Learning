import sqlite3

# creating connection
conn = sqlite3.connect("./Sqlite_Database_practice/customer.db")

# creating cursor 
cursor = conn.cursor()

# data of users
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

# # inserting a single data row
# # cursor.execute("INSERT INTO customers VALUES ('Rohit', 'Singh', 'rohit.singh11299@gmail.com')")

# inserting into Table
cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

cursor.execute("SELECT rowid, * FROM customers")

items = cursor.fetchall()

print(f"S.No \t\tFirst Name \t\tLast Name \t\tEmail")
print("---\t\t\t-------\t\t\t------\t\t\t----------------------")
for item in items:
    print(f"{item[0]} \t\t\t{item[1]} \t\t\t{item[2]} \t\t\t{item[3]}")

conn.commit()
conn.close()