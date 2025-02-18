import requests
import pprint
import json
import pandas as pd


s = requests.Session()
s.headers.update({'Authorization': 'Bearer deb79eea-1eee-430d-9632-1e987aa46c15'})
s.headers.update({'Accept': 'application/json'})
url = f"https://www.rejseplanen.dk/api/"
#access = f"accessId=deb79eea-1eee-430d-9632-1e987aa46c15"
myrep = s.get(url+f"linematch?match=2&operators=NT")
#print(myrep.headers)
#print(myrep.json())

myrep = s.get(url+f"lineinfo?lineId=028_280_06_2&date=2025-02-17")
#print(myrep.json())

myrep = s.get(url+f"location.name?input=eternitten&type=S&name=Bus 2&maxNo=2")
#print(myrep.json())

#851030703
#A=1@O=Eternitten (Østre Allé / Aalborg)@X=9937054@Y=57038111@U=86@L=851030703@B=1@p=1739790541
#A=1@O=Eternitten (Bornholmsgade / Aalborg)@X=9935795@Y=57038228@U=86@L=851008902@
myrep = s.get(url+f"multiArrivalBoard?idList=A=1@O=Eternitten (Bornholmsgade / Aalborg)@X=9935795@Y=57038228@U=86@L=851008902@&date=2025-02-20&time=08:00&duration=60")
#print(myrep.json())
fdict=myrep.json()

def filterdic(pairs):
    key,value = pairs
    filter_value = "2"
    if value == filter_value:
        return True
    else:
        return False

l1=fdict["Arrival"]

i=0
for x in l1:
    if l1[i]["name"] == "Bybus 2":
        pp = pprint.PrettyPrinter(depth=4)
        pp.pprint(l1[i]["time"])
    i = i+1

#stops = [entries for entries in jdict if entries["name"] == "Bybus 2"]


#outdict = [x for x in jdict if x[&quot;age&quot;&gt;] "Bybus 2"]
#finout = json.dumps(jdict)
#print(finout)