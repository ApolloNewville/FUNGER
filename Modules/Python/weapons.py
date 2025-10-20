import pandas as pd
import numpy as np
from dataframe_creation import dfs

# Creation of an independent dataframe
Weapons = pd.DataFrame(dfs["Weapons"]).replace("",np.nan).dropna(how='any',subset=['name','description'])
print(Weapons['params'])