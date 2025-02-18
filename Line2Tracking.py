import requests
import pprint
import json
import pandas as pd

from Line2 import vdb

s = requests.Session()
s.headers.update({'Authorization': 'Bearer deb79eea-1eee-430d-9632-1e987aa46c15'})
s.headers.update({'Accept': 'application/json'})
url = f"https://www.rejseplanen.dk/api/"

print(vdb.upcode)

#myrep = s.get(url+f"multiArrivalBoard?idList="+ vdb.upcode + f"&date=2025-02-20&time=08:00&duration=60")
myrep = s.get(url+f"multiArrivalBoard?idList=A=1@O=Væddeløbsbanen (Skydebanevej / Aalborg)@X=9882660@Y=57054678@U=86@L=851007302@B=1@p=1739892283@&date=2025-02-20&time=08:00&duration=60")
fdict=myrep.json()
#l1=fdict["Arrival"]
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(fdict)