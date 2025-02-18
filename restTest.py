import requests
import pprint
import json
import pandas as pd


s = requests.Session()
s.headers.update({'Authorization': 'Bearer deb79eea-1eee-430d-9632-1e987aa46c15'})
s.headers.update({'Accept': 'application/json'})
url = f"https://www.rejseplanen.dk/api/"
#access = f"accessId=deb79eea-1eee-430d-9632-1e987aa46c15"
#myrep = s.get(url+f"linematch?match=2&operators=NT")
#print(myrep.headers)
#print(myrep.json())

#myrep = s.get(url+f"lineinfo?lineId=028_280_06_2&date=2025-02-17")
#print(myrep.json())

myrep = s.get(url+f"location.name?input=Væddeløbsbanen&type=S")
pp = pprint.PrettyPrinter(depth=4)
#pp.pprint(myrep.json())

#851030703
ost = "A=1@O=Eternitten (Østre Allé / Aalborg)@X=9937054@Y=57038111@U=86@L=851030703@B=1@p=1739790541"
born = "A=1@O=Eternitten (Bornholmsgade / Aalborg)@X=9935795@Y=57038228@U=86@L=851008902@"
ved = "A=1@O=Væddeløbsbanen (Skydebanevej / Aalborg)@X=9881159@Y=57054184@U=86@L=851007301@B=1@p=1739892283@"
jom = "A=1@O=Jomfru Ane Gade (Borgergade / Aalborg)@X=9918212@Y=57050957@U=86@L=851002402@B=1@p=1739892283@"
myrep = s.get(url+f"multiArrivalBoard?idList="+born+f"&date=2025-02-20&time=08:00&duration=60")
#print(myrep.json())
fdict=myrep.json()

l1=fdict["Arrival"]

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(l1)

i=0
"""
for x in l1:
    if l1[i]["name"] == "Bybus 2":
        pp = pprint.PrettyPrinter(depth=4)
        pp.pprint(l1[i]["time"])
    i = i+1
"""
#stops = [entries for entries in jdict if entries["name"] == "Bybus 2"]


#outdict = [x for x in jdict if x[&quot;age&quot;&gt;] "Bybus 2"]
#finout = json.dumps(jdict)
#print(finout)