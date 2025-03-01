import requests
import pprint
import json
import pandas as pd
import numpy as np
from datetime import datetime 
from Line2 import ett
import timedelta as td
import time

day = datetime.today().strftime('%Y-%m-%d')
tim = datetime.today().strftime('%H:%M')

s = requests.Session()
s.headers.update({'Authorization': 'Bearer deb79eea-1eee-430d-9632-1e987aa46c15'})
s.headers.update({'Accept': 'application/json'})
url = f"https://www.rejseplanen.dk/api/"

#myrep = s.get(url+f"multiArrivalBoard?idList="+ett.downcode+"|"+ett.upcode+f"&date="+day+f"&time="+tim+"&duration=10")
#fdict=myrep.json()
#l1=fdict["Arrival"]
#pp = pprint.PrettyPrinter(depth=4)
#pp.pprint(l1)

nextBusUp = np.array([">10", ">10", ">10"])
nextBusDown = np.array([">10", ">10", ">10"])

while 1:
    day = datetime.today().strftime('%Y-%m-%d')
    tim = datetime.today().strftime('%H:%M')
    deltaT = td.Timedelta()
    myrep = s.get(url+f"multiArrivalBoard?idList="+ett.downcode+"|"+ett.upcode+f"&date="+day+f"&time="+tim+"&duration=30")
    fdict=myrep.json()
    ettBoard = fdict["Arrival"]
    i = 0
    j= 0
    for x in ettBoard:
        if (ettBoard[i]["origin"].startswith("AAU Bus")) or (ettBoard[i]["origin"].startswith("Aalborg Universitets")):
            ettUpArrN = ettBoard[i]["name"]
            ettUpArrT = ettBoard[i]["time"]
            ettUpArrT = datetime.strptime(ettUpArrT,'%H:%M:%S')
            if ettUpArrN == "Bybus 2":
                arrD = td.Timedelta(ettUpArrT - datetime.strptime(tim,'%H:%M'))
                if arrD >= deltaT:
                    nextTwoUp = str(arrD.total.minutes)
                    upField = f"The next 2 towards town is in " + nextTwoUp + f" minutes"
                    print ("\r" + upField + "        ", end='')
                    break
        i = i+1

 
    time.sleep(60)

