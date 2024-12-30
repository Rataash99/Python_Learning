import sqlite3

conn = sqlite3.connect("/Sqlite_Database_practice/customer.db")
cursor = sqlite3.cursor()

items = cursor.fetchall()

