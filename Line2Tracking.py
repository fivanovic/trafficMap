import requests
import pprint
import json
import pandas as pd
import numpy as np
from datetime import datetime 
from Line2 import bybus2, ett
import timedelta as td
import time
from utils import updownTime

day = datetime.today().strftime('%Y-%m-%d')
tim = datetime.today().strftime('%H:%M')

s = requests.Session()
s.headers.update({'Authorization': 'Bearer deb79eea-1eee-430d-9632-1e987aa46c15'})
s.headers.update({'Accept': 'application/json'})
url = f"https://www.rejseplanen.dk/api/"

#myrep = s.get(url+f"multiArrivalBoard?idList="+ett.downcode+"|"+ett.upcode+f"&date="+day+f"&time="+tim+"&duration=30")
#fdict=myrep.json()
#pp = pprint.PrettyPrinter(depth=5)
#pp.pprint(fdict)

while 1:
    day = datetime.today().strftime('%Y-%m-%d')
    tim = datetime.today().strftime('%H:%M')
    deltaT = td.Timedelta()
    myrep = s.get(url+f"multiArrivalBoard?idList="+ett.downcode+"|"+ett.upcode+f"&date="+day+f"&time="+tim+"&duration=30")
    fdict=myrep.json()
    ettBoard = fdict["Arrival"]
    i = 0

    twoUp,twoDown = updownTime(ettBoard,ett.name,i,ett.upname,ett.upname2,ett.downname,bybus2.lineName,tim,deltaT)

    print ("\r" + f"Next 2 towards town is in " + twoUp + f" minutes and the next 2 towards Uni is in " + twoDown + f" minutes" + "        ", end='')
    time.sleep(60)


   

