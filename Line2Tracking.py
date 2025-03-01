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

nextBusUp = np.array([">10", ">10", ">10"])
nextBusDown = np.array([">10", ">10", ">10"])
"""
myrep = s.get(url+f"multiArrivalBoard?idList="+ett.downcode+"|"+ett.upcode+f"&date="+day+f"&time="+tim+"&duration=30")
fdict=myrep.json()
pp = pprint.PrettyPrinter(depth=5)
pp.pprint(fdict)
"""

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
        #if (ettBoard[i]["origin"].startswith("Vædd")):
            ettUpArrN = ettBoard[i]["name"]
            ettUpArrT = ettBoard[i]["time"]
            ettUpArrT = datetime.strptime(ettUpArrT,'%H:%M:%S')
            if ettUpArrN == "Bybus 2":
                arrD = td.Timedelta(ettUpArrT - datetime.strptime(tim,'%H:%M'))
                if arrD >= deltaT:
                    nextTwoUp = str(arrD.total.minutes)
                    upField = f"The next 2 towards town is in " + nextTwoUp + f" minutes "
                    break
        i = i+1
    i = 0
    for x in ettBoard:
        if (ettBoard[i]["origin"].startswith("Vædd")):
            ettDownArrN = ettBoard[i]["name"]
            ettDownArrT = ettBoard[i]["time"]
            ettDownArrT = datetime.strptime(ettDownArrT,'%H:%M:%S')
            if ettDownArrN == "Bybus 2":
                arrD = td.Timedelta(ettDownArrT - datetime.strptime(tim,'%H:%M'))
                if arrD >= deltaT:
                    nextTwoDown = str(arrD.total.minutes)
                    downField = f"and the next 2 towards Uni is in " + nextTwoDown + f" minutes"
                    break
        i = i+1

    print ("\r" + upField + downField + "        ", end='')
    time.sleep(60)

