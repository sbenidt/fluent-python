import pandas as pd

df = pd.read_csv("FirstGenPokemon.csv")

# filter to needed columns
col_list = [
    ' Name',
    'Number',
    ' Type1',
    ' Type2',
    ' Height(m)',
    ' Weight(kg)',
]
df = df.loc[:, col_list]

# rename columns
col_names = [
    'name',
    'number',
    'type1',
    'type2',
    'height_m',
    'weight_kg',
]
df.columns = col_names

# write to csv
df.to_csv("pokemon_1st_gen_cleaned.csv", index=False)
