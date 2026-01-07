# Modules
import pandas as pd
from Load.data_loading import extraction
from Transformation.cleaning import df_cleaning
# Paths
folder_path = r'Data\raw data'
files_interest = ['Weapons','Skills','Armors','Classes','Enemies']


dfs = extraction(path = folder_path,
                 keywords = files_interest)

dfs = dfs.copy()

for key, df in dfs.items():
    dfs[key] = df_cleaning(df=df, dropna_how='all')

print(dfs)