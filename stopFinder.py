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

myrep = s.get(url+f"location.name?input=Aalborg Vestby St&type=S")
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(myrep.json())

#UT = "A=1@O=Aalborg Vestby St. (Kastetvej / Aalborg Vestby St)@X=9908603@Y=57052665@U=86@L=851121902@B=1@p=1740743877@"

myrep = s.get(url+f"multiArrivalBoard?idList="+UT+f"&date="+day+f"&time="+tim+f"&duration=20")
fdict=myrep.json()
l1=fdict["Arrival"]
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(l1)