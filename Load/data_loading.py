import pandas as pd
import json
from pathlib import Path
import numpy as np

"""
The objective of this element is extracting all data from all dictionaries to convert them into data frames.
Each data frame will be called by a key, element obtained from the name of the file and the values will be 
by itself the data frame.
"""

# This function loads JSON files that their file names matches with the list of files of interest.
def extraction(path: str,
               keywords: list):
    path = Path(path)
    dfs = {}
    for file in path.glob('*.json'):
        if file.stem in keywords:
            with open(file) as f:
                json_file = json.load(f)
            df = pd.json_normalize(json_file)
            dfs[file.stem] = df
    return  dfs