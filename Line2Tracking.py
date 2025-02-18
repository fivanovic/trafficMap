import requests
import pprint
import json
import pandas as pd

from Line2 import vdb, ett

s = requests.Session()
s.headers.update({'Authorization': 'Bearer deb79eea-1eee-430d-9632-1e987aa46c15'})
s.headers.update({'Accept': 'application/json'})
url = f"https://www.rejseplanen.dk/api/"

#myrep = s.get(url+f"multiArrivalBoard?idList="+ vdb.upcode + f"&date=2025-02-20&time=08:00&duration=60")
myrep = s.get(url+f"multiArrivalBoard?idList="+vdb.upcode+"|"+ett.upcode+f"&date=2025-02-20&time=10:00&duration=10")
fdict=myrep.json()
l1=fdict["Arrival"]
pp = pprint.PrettyPrinter(depth=4)
#pp.pprint(l1)
i=0


#this is going to be the upstream method for IDing 
for x in l1:
    if (l1[i]["origin"].startswith("AAU Bus")) or (l1[i]["origin"].startswith("Aalborg Universitets")): 
        pp = pprint.PrettyPrinter(depth=4)
        pp.pprint(l1[i]["stop"])
        pp.pprint(l1[i]["time"])
    i = i+1
