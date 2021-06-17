"""Code to illustrate the power of the python data model by creating a pokedex class"""

import collections
from random import choice

# Create Pokemon Class
Pokemon = collections.namedtuple(
    "Pokemon",
    ["name", "number", "type1", "type2", "height", "weight", "catch_status"])


# Create Pokedex Class
class Pokedex:
    """The Pokedex Class implements the 1st Gen Pokedex from Pokemon Red/Blue/Yellow
    and keep track of pokemon either not seen, seen, or caught

    """
    def __init__(self):
        with open("pokemon_1st_gen_cleaned.csv") as filen:
            pokemon_data = filen.read()
            # skip header row
            pokemon_data = pokemon_data.splitlines()[1:]
        self._pokemon = []
        for row in pokemon_data:
            row = row.split(',')
            pokemon_iter = Pokemon(name=row[0],
                                   number=int(row[1]),
                                   type1=row[2],
                                   type2=row[3],
                                   height=float(row[4]),
                                   weight=float(row[5]),
                                   catch_status="Not_Seen")
            self._pokemon.append(pokemon_iter)

    def seen(self, name):
        """Change catch status of Pokemon to Seen if not already Caught

        Parameters:
        ----------
        name: str,
            name of 1st Gen Pokemon

        Returns:
        -------
        None
        """
        position = self._get_position(name)
        old_pokemon = self[position]
        if old_pokemon.catch_status == "Caught":
            print(f"{self[position].name} has already been Caught")
        else:
            new_pokemon = Pokemon(*old_pokemon[:-1], catch_status='Seen')
            self._pokemon[position - 1] = new_pokemon
            print(f"{self[position].name} has been Seen")

    def caught(self, name):
        """Change catch status of Pokemon to Caught

        Parameters:
        ----------
        name: str,
            name of 1st Gen Pokemon

        Returns:
        -------
        None
        """
        position = self._get_position(name)
        old_pokemon = self[position]
        new_pokemon = Pokemon(*old_pokemon[:-1], catch_status='Caught')
        self._pokemon[position - 1] = new_pokemon
        print(f"{self[position].name} has been Caught")

    def __len__(self):
        """Get length of Pokedex Class"""
        return len(self._pokemon)

    def __getitem__(self, item):
        """Look up pokemon by position, slices, or name"""
        if isinstance(item, slice):
            # Support Slicing
            # Support pokedex incides starting with 1 instead of 0
            start = item.start - 1
            stop = item.stop - 1
            step = item.step
            return self._pokemon[slice(start, stop, step)]
        elif isinstance(item, str):
            # Support pokemon lookup by name
            position = self._get_position(item)
        else:
            position = item
        # Support pokedex incides starting with 1 instead of 0
        return self._pokemon[position - 1]

    def _get_position(self, name):
        """Get pokemon number given pokemon name

        Parameters:
        ----------
        name: str,
            name of 1st Gen Pokemon

        Returns:
        -------
        number: int,
            pokemon's pokedex number
        """
        position_list = [
            pokemon.number for pokemon in self._pokemon
            if pokemon.name.lower() == name.lower()
        ]
        if len(position_list) == 0:
            raise ValueError("Pokemon Name not in Pokedex")
        else:
            return position_list[0]

    def _evaluate(self):
        """Evaluate your Pokedex. Prints a message indicating number of pokemon seen and caught"""
        num_caught = len([
            pokemon for pokemon in self._pokemon
            if pokemon.catch_status == 'Caught'
        ])
        num_seen = len([
            pokemon for pokemon in self._pokemon
            if pokemon.catch_status == 'Seen'
        ])
        num_seen += num_caught
        # print("\n")
        # print(
        #     "Good to see you! How is your Pokédex coming? Here, let me take a look!"
        # )
        # print("\n")
        # print("Professor Oak's Pokedex Evaluation:")
        # print(f"Number of Pokemon Seen: {num_seen}")
        # print(f"Number of Pokemon Caught: {num_caught}")

        message_list = [
            "You still have lots to do. Look for Pokémon in grassy areas!",
            "You're on the right track! Get a Flash HM from my Aide!",
            "You still need more Pokémon! Try to catch other species!",
            "Good, you're trying hard! Get an Itemfinder from my Aide",
            "Looking good! Go find my Aide when you get 50!",
            "You finally got a least 50 species! Be sure to get Exp.All from my Aide!",
            "Ho! This is getting even better!",
            "Very good! Go fish for some marine Pokémon!",
            "Wonderful! Do you like to collect things?",
            "I'm impressed! It must have been difficult to do!",
            "You finally got at least 100 species I can't believe how good you are!",
            "You even have the evolved forms of Pokémon! Super!",
            "Excellent! Trade with friends to get some more!",
            "Outstanding! You've become a real pro at this!",
            "I have nothing left to say! You're the authority now!",
            "Your Pokédex is entirely complete! Congratulations!",
        ]

        message_index = num_caught // 10
        message = message_list[message_index]
        # print("\n")
        # print(message)
        print_message_list = [
            "\n",
            "Good to see you! How is your Pokédex coming? Here, let me take a look!",
            "\n", "Professor Oak's Pokedex Evaluation:", "\n",
            f"Number of Pokemon Seen: {num_seen}", "\n",
            f"Number of Pokemon Caught: {num_caught}", "\n", message
        ]
        print_message = "".join(print_message_list)
        return print_message

    def __repr__(self):
        return self._evaluate()


if __name__ == "__main__":

    # Create a dex
    dex = Pokedex()

    # Check out the repr message for the class
    dex

    # By implementing __len__ the pokedex has a length
    len(dex)

    # Can look up the 121st pokemon since __getitem__ is implemented
    dex[121]

    # slicing is also supported
    dex[120:125]

    # Look Up Pokemon by Name
    dex["Squirtle"]

    # Can sort the pokedex
    sorted(dex)[:5]

    # sort by height, then weight
    sorted(dex, key=lambda x: (x.height, x.weight))[:5]

    # Select a random pokemon
    choice(dex)

    # Can iterate over the pokedex
    for pokemon in dex:
        if pokemon.type1 == 'dragon':
            print(pokemon)

    # Catch a Pokemon
    dex.seen("Alakazam")
    dex.caught("Mewtwo")

    # Get all Caught Pokemon
    [pokemon for pokemon in dex if pokemon.catch_status == 'Caught']

    # Evaluate your Pokedex
    dex
