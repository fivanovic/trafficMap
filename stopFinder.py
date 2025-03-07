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

myrep = s.get(url+f"location.name?input=AAU Busterminal (Sigrid Undsetsvej / Aalborg)&type=S")
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(myrep.json())

UT = "A=1@O=AAU Fr.Bajers Vej (Bertil Ohlins Vej / Aalborg)@X=9983851@Y=57014919@U=86@L=851991602@B=1@"

myrep = s.get(url+f"multiArrivalBoard?idList="+UT+f"&date="+day+f"&time="+tim+f"&duration=20")
fdict=myrep.json()
l1=fdict["Arrival"]
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(l1)