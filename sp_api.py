import pandas as pd
import requests

def sp_api():
    sp = requests.get('https://swapi.dev/api/species%27).json()
    return sp
