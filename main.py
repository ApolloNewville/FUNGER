# Modules
import pandas as pd
from Load.data_loading import extraction
from Transformation.cleaning import df_cleaning, str_cleaning
# Paths
folder_path = r'Data\raw data'
files_interest = ['Weapons','Skills','Armors','Classes','Enemies']

# Extraction of JSON data and convertion to data frames inside of the dictionary called dfs.
dfs = extraction(path = folder_path,
                 keywords = files_interest)

# Creation of a copy from dictionary dfs
dfs = dfs.copy()


# Iteration to clean data frames from dictionary dfs
for key, df in dfs.items():
    df = df_cleaning(df=df, dropna_how='all')
    df = str_cleaning(df=df)
    dfs[key] = df

print(dfs)