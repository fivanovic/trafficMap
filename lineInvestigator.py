import requests
import pprint
import json
import pandas as pd
from datetime import datetime 
import numpy as np

day = datetime.today().strftime('%Y-%m-%d')
tim = datetime.today().strftime('%H:%M')

s = requests.Session()
s.headers.update({'Authorization': 'Bearer deb79eea-1eee-430d-9632-1e987aa46c15'})
s.headers.update({'Accept': 'application/json'})
url = f"https://www.rejseplanen.dk/api/"

myrep = s.get(url+f"lineinfo?lineId=028_280_06_2&date="+day)
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(myrep.json())