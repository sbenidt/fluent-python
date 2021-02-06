import pandas as pd

df = pd.read_csv("pokemon.csv")

# filter to needed columns
col_list = [
    'name',
    'pokedex_number',
    'type1',
    'type2',
    'height_m',
    'weight_kg',
    'generation',
]
df = df.loc[:, col_list]

# filter to gen 1 pokemon
filt = (df.generation == 1)
df = df.loc[filt, :]

# drop gen column
df = df.drop('generation', axis=1)

# write to csv
df.loc[filt, :].to_csv("pokemon_1st_gen.csv", index=False)
