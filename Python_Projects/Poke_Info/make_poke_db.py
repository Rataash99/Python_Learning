from create_poke_db import create_table, insert_data
from pokemon_data import pokemons as pokeys, get_poke_list

url = "/db/pokemons.db"
db_name = "pokemons"

entities = [
    "name",
    "abilities",
    "base_experience",
    "forms",
    "height",
    "moves"
]
print('successful')

# pokemons = get_poke_list(pokeys)

# create_table(url, db_name, entities)
# insert_data(url, db_name, pokemons)
