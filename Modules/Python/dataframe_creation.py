import pandas as pd
import json
from pathlib import Path

path = Path(r'Data')

# The names of the files of interest
files_of_interest = ("Items","Weapons","Armors","Enemies")

# Global dictionary
global_dictionary = {}

# Loading all files in the folder
for file in path.glob('*.json'):
    if file.stem in files_of_interest:
        with open(file, 'r',encoding='utf-8') as f:
            global_dictionary[file.stem] = json.load(f)

common_keys = set.intersection(*(set(inner.keys()) for inner in global_dictionary.values()))
print(common_keys)