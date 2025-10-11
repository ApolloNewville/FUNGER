import pandas as pd
import json
from pathlib import Path


folder = Path(r"Data") # Location of all data files from Fear and Hunger 2 Termina
fi = ["Items","Characters","Enemies","Armour"] # Files of interest

# Extraction of all files of interest

dfs = {} # dfs mean dataframes, it is which contains all dataframes per file

fi = [file for file in folder.glob("*.json") # Files of interest
  if any(word in file.name for word in fi)]

for file in fi:
    with open("r",folder,encoding="utf-8") as f:
        json.load(f) # Loads json file to work with
        df = pd.json_normalize(f) # Normalization of JSON to data frame
        kn = file.stem # Assignation of the name with no file extension as the name of the data frame
        dfs[kn] = df # Naming data frame as the name of the file.