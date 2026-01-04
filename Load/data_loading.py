import pandas as pd
import json
from pathlib import Path
import numpy as np

# This is the process to extract data from the JSON files and create data frames which will be inside of other dictionaries.
##  General dictionary -> Data frame with name key -> Data frame

# interfaces de interacción

def extraction(path,keywords):
    path = Path(path)
    dfs = {}
    for file in path.glob('*.json'):
        if file.stem in keywords:
            with open(file) as f:
                json_file = json.load(f)
            df = pd.json_normalize(json_file)
            dfs[file.stem] = df
    return  dfs

def df_cleaning(df):
    if isinstance(df,pd.DataFrame):
        df = df.replace('',np.nan)
        df = df.dropna(how='all',axis='index')
    return df

def dict_cleaning(dictionary):
    if isinstance(dictionary,dict):
        for name, df in dictionary.items():
            dictionary[name] = df_cleaning(df)
    return dictionary, print('This is the global dictionary \n',dictionary)