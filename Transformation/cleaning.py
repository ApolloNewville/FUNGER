import pandas as pd
import numpy as np
import re
from typing import Literal

# This is the re pattern to determine columns that only has integers.
number_re = re.compile(r'^\d+(\.\d+)?$')  

# This is 

def df_cleaning(
        df: pd.DataFrame,
        dropna_how: Literal['any','all'] = 'any') -> pd.DataFrame:
    # Validation of inputs
    if dropna_how not in ('all','any'): 
        raise ValueError('Write all or any to declare the process of dropna')    
    # Removing '' values from data frames
    df = df.replace(to_replace='',value=np.nan).replace(to_replace=r'[\n\t]|\\n|\\t',value=' ',regex=True)
    df = df.infer_objects(copy=False)
    df = df.dropna(how=dropna_how,axis='index').dropna(subset=['name'])
    return df

def str_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    if not isinstance(df,pd.DataFrame):
        raise TypeError('Object must be a pd.DataFrame')
    def clean_cell(x:str):
        return x.strip().lower() if isinstance(x,str) else x
    return df.copy().apply(lambda col: col.map(clean_cell))