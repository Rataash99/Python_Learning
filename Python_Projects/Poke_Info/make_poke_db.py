from create_poke_db import create_table, insert_data, print_data
from pokemon_data import pokemons

url = "./db/pokemon.db"
db_name = "pokemons"

entities = [
    "name text",
    "abilities text",
    "base_experience integer",
    "forms text",
    "height integer",
    "moves text"
]
# create_table(url, db_name, entities)
insert_data(url, db_name, pokemons)

print_data(url, db_name)
