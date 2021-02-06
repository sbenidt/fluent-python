"""Code to illustrate python data model by creating a pokedex class"""

import collections
from random import choice

# Create Pokemon Class
Pokemon = collections.namedtuple(
    "Pokemon", ["name", "number", "type1", "type2", "height", "weight"])


# Create Pokedex Class
class Pokedex:
    def __init__(self):
        with open("pokemon_1st_gen.csv") as filen:
            pokemon_data = filen.read()
            # skip header row
            pokemon_data = pokemon_data.splitlines()[1:]
        self._pokemon = [Pokemon(*row.split(',')) for row in pokemon_data]

    def __len__(self):
        return len(self._pokemon)

    def __getitem__(self, position):
        # Support pokedex incides starting with 1 instead of 0
        if isinstance(position, slice):
            start = position.start - 1
            stop = position.stop - 1
            step = position.step
            return self._pokemon[slice(start, stop, step)]
        else:
            return self._pokemon[position - 1]


if __name__ == "__main__":

    # Create a dex
    dex = Pokedex()

    # By implementing __len__ the pokedex has a length
    len(dex)

    # Look up the 121st pokemon
    dex[121]

    # slicing is supported
    dex[120:130]

    # Can sort the pokedex
    sorted(dex)

    # sort by height, then weight
    sorted(dex, key=lambda x: (x.height, x.weight))

    # can reverse sort
    list(reversed(dex))

    # Select random pokemon
    choice(dex)

    # containment is implemented
    onix = Pokemon(
        name='Onix',
        number='95',
        type1='rock',
        type2='ground',
        height='8.8',
        weight='210.0')
    onix in dex
