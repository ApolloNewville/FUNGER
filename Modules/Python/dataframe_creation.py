import csv
import pandas as pd
import json
from pathlib import Path as P

# Load fear and hunger folder
folder = P(r"c:\Program Files (x86)\Steam\steamapps\common\Fear & Hunger 2 Termina\www\data")

# Key words

kw = ["Items","Enemies","Weapons","Armors"]

# Normalize data

filtered_files = [file for file in folder.glob("*.json")
                  if any (word in file.name for word in kw)]

dfs = []

for file in filtered_files:
    with open(file, "r", encoding='utf-8') as f:
        data = json.load(f)
        df = pd.json_normalize(data)
        df.dropna(how='all',inplace=True)
        dfs.append(df)
        print(f"Nombre del archivo: {file.name}")
        print(f"Lista de columnas: {df.columns}")
        print(df.head(4))

# Obtention of all common columns

cc = set(dfs[0].columns) # In this case, I just make a set of all columns from the first dataframe.

# Filtration and obtation of the common columns

for i, df in enumerate(dfs):
    cc = set(df.columns)

# Just keeping intersected columns from each data frame

## Iteration to each column

for i, df in enumerate(dfs):
    cc = set(df.columns)



""""
intersección (&=)
for i, df in enumerate(dfs):
    columnas_actuales = set(df.columns)
    
    # Mantener solo las columnas que nos interesan
    columnas_actuales &= columnas_interes
    
    # Reasignamos el DataFrame con solo esas columnas
    dfs[i] = df[list(columnas_actuales)]

# Revisamos el resultado
for df in dfs:
    print(df.columns)
"""