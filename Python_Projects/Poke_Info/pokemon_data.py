from Controller.get_poke_data import fetch_data
import json

url = "https://pokeapi.co/api/v2/pokemon"
data = fetch_data(url)

class Pokemon:
    def __init__(self, name, abilities, base_exp, forms, height, moves):
        self.name = name
        self.abilities = abilities
        self.base_experience = base_exp
        self.forms = forms
        self.height = height
        self.moves = moves

    def get(self):
        info = [
            self.name,
            json.dumps(self.abilities),
            self.base_experience,
            json.dumps(self.forms),
            self.height,
            json.dumps(self.moves)
        ]
        return info

pokemons_list = data.get('results', [])

# function definition for getting pokemon abilities
def get_abilities(data):
    abilities = []
    for entries in data:
        ability = entries.get("ability").get('name')
        abilities.append(ability)

    return abilities

# function definition for getting pokemon forms
def get_forms(data):
    forms = []
    for form in data:
        forms.append(form.get('name'))

    return forms

# function definition for getting pokemon moves
def get_moves(data):
    moves = []

    for entry in data:

        move = entry.get('move')
        name = move.get('name')

        moves.append(name)

pokemons = [] 

# adding pokemmons to pokemons list
for pokemon in pokemons_list:

    poke_url = pokemon.get('url')

    # getting name of the pokemon
    name = pokemon.get('name')

    # fetching data of a particular pokemon
    poke_data = fetch_data(poke_url)

    # height of the pokemon
    height = poke_data.get('height')

    # pokemon base experience
    base_exp = poke_data.get("base_experience")

    # getting pokemon abilities
    abilities = get_abilities(poke_data.get("abilities"))

    # getting pokemon forms
    forms = get_forms(poke_data.get('forms'))

    # getting pokemon moves
    moves = get_moves(poke_data.get('moves'))
    # pokemons_list.append(entries.name)

    poke = Pokemon(
        name,
        abilities,
        base_exp,
        forms,
        height,
        moves
    )
    pokemons.append(poke)

def get_poke_list(pokemons):
    return pokemons
