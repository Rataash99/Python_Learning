import sqlite3
from pokemon_data import get_poke_list

def create_table(url, name, entities):
    conn = sqlite3.connect(url)
    cursor = conn.cursor()

    placeholder = ", ".join(entities)

    cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} ({placeholder})")

    conn.commit()
    conn.close()

def insert_data(url, name, data):
    conn = sqlite3.connect(url)
    cursor = conn.cursor()


    cols = len(data)
    query_size = ", ".join(["?"] * cols)
    processed_data = [pokemon.get() for pokemon in data]

    query = f"INSERT INTO {name} VALUES ({query_size})"

    cursor.executemany(query, processed_data)

    conn.commit()
    conn.close()

