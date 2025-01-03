import sqlite3

def show_poke_db(url, name):
    conn = sqlite3.connect(url)
    cursor = conn.cursor()

    cursor.execute(f"SELECT rowid, * FROM {name}")

    items = cursor.fetchall()

    print(items)

    