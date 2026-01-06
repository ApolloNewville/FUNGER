import pandas as pd
from Load.data_loading import extraction

folder_path = r'Data\raw data'
files_interest = ['Weapons','Skills','Armors','Classes','Enemies']

dfs = extraction(path = folder_path,
                 keywords = files_interest)

dfs = dfs.copy()

# Cleaning step
for key, values in dfs.items():
    dfs[key] = values.dropna(how='all')