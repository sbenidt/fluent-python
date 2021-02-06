import collections

# Create Pokemon Class
Pokemon = collections.namedtuple(
    "Pokemon", ["name", "number", "type1", "type2", "height", "weight"])

# Create Pokedex Class
class Pokedex:
    def __init__(self):
        with open("pokemon_1st_gen.csv") as filen:
            pokemon_data = filen.read()
            pokemon_data = pokemon_data.splitlines()
        self._pokemon = [Pokemon(*row.split(',')) for row in pokemon_data]

    def __len__(self):
        return len(self._pokemon)

    def __getitem__(self, position):
        return self._pokemon[position]
