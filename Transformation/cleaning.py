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
    if dropna_how not in ('all','any'): 
        raise ValueError('Write all or any to declare the process of dropna')    
    df = df.replace(to_replace='',value=np.nan)
    df = df.infer_objects(copy=False)
    df = df.dropna(how=dropna_how,axis='index')
    return df

def cleaning_column(column: pd.Series):
    column.str.strip().str.lower()