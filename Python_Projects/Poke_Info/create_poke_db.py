import sqlite3
import json

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
    processed_data = []

    cols = 6
    query_size = ", ".join(["?"] * cols)

    for pokemon in data:
        abilities = json.dumps(pokemon.abilities)
        moves = json.dumps(pokemon.moves)
        forms = json.dumps(pokemon.forms)

        processed_data.append((
            pokemon.name,
            abilities,
            pokemon.base_experience,
            forms,
            pokemon.height,
            moves
        ))

    query = f"INSERT INTO {name} VALUES ({query_size})"
    cursor.executemany(query, processed_data)

    conn.commit()
    conn.close()

def print_data(url, name):

    conn = sqlite3.connect(url)
    cursor = conn.cursor()
    cursor.execute(f"SELECT rowid, * FROM {name}")
    items = cursor.fetchall()
    print(items)