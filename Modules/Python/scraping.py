import requests
from bs4 import BeautifulSoup 
import json
import pandas as pd

# Requests is to obtain and download whole information from the page, requesting it from the holder sever.
page = requests.get(r'https://fearandhunger.fandom.com/wiki/Termina_Items_List')

if page.status_code == 200:
    print("Conection sucessfully done!:)")
else: 
    print(f"There were any trounble with the conection to the server! {page.status_code}")

soup = BeautifulSoup(page, 'html-parser')