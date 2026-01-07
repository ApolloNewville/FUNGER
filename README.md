# FUNGER

Fear and Hunger 2 Termina is a rolplay game that involves different data to win.

The data of interest are the next one: Items, Armors, Skills and Enemies.

The objetive of this project are the next one:
1. Import JSON data from the game in.
2. Load data into a python script to convert them into data frames.
3. Develop an exploratoy analysis to determine what are the critical elements from data frames. (The exploratory analysis will require their own objectives).
4. Upload data into a designed database to make videos in the future on YouTube.


# Elemental things to know:
There is a ETL pipeline focuses on extract data from the different JSON files. Especially from certain JSON files named: Armors, Skills, Weapons, Items and Enemies. This files are extracted and normalized by pandas tools by this way:

```import pandas as pd
from pathlib import Path
files_interes = ['Weapons','Items','Enemies','Skills','Armors']
folder_path = <folder_path>'```
