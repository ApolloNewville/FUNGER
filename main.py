# Modules
import pandas as pd
from Load.data_loading import extraction
from Transformation.cleaning import df_cleaning, str_cleaning


def main(): # This main function is for 

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

    for key, value in dfs.items():
        print(key)
        print(list(value.columns))

    dfs['Weapons']['damage'] = dfs['Weapons']['params'].apply(lambda row: row[2])
    print(dfs['Weapons'][['name','description','price','damage']].sort_values(by=['name'], ascending = True))

if __name__ == "__main__":
    main()  