import sqlite3

# creating a table
def create_table(db_url, db_name, entities):
    conn = sqlite3.connect(db_url)
    placeholder = ", ".join(entities)
    cursor = conn.cursor()

    cursor.execute(f"CREATE TABLE {db_name} ({placeholder})")


# inserting a single row in table
def insert_one(row_data, db_url, db_name):

    # creating connection 
    conn = sqlite3.connect(db_url)
    
    # creating cursor
    cursor = conn.cursor()

    # insert in table
    cursor.execute(f"INSERT INTO {db_name} VALUES {row_data}")

    conn.commit()
    conn.close()

def insert_many(data, db_url, db_name):
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()

    # num of cols contained by table
    num_cols = len(data)

    # generatign num of queries that needs to be added
    query_size = ", ".join(["?"] * num_cols)

    # query for inserting 
    query = f"INSERT INTO {db_name} VALUES ({query_size})"

    # inserting many values in table
    cursor.executemany(query, data)

    conn.commit()
    conn.close()

# updating table row
def update_table(entity, change, rid, db_url, db_name):
    conn = sqlite3.connect(db_url)

    cursor = conn.cursor()
    cursor.execute(f"UPDATE {db_name} SET {entity} = '{change}' WHERE rowid = {rid}")

    conn.commit()
    conn.close()

def delete_table(db_url, db_name):
    conn = sqlite3.connect(db_url)

    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE {db_name}")

    conn.commit()
    conn.close()

def delete_records(db_url, db_name, rid):
    conn = sqlite3.connect(db_url)

    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {db_name} WHERE rowid = {rid}")

    conn.commit()
    conn.close()

def show_db_entries(db_url, db_name):
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()

    cursor.execute(f"SELECT rowid, * FROM {db_name}")

    items = cursor.fetchall()

    print(items)        