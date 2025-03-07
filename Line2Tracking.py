import requests
import pprint
import json
import pandas as pd
import numpy as np
from datetime import datetime 
from Line2 import bybus2,vdb,vfw,hld,avs,jag,nyt,aas,jlg,kld,ett,sgp,dal,glt,sbs,plp,gnt,ptp,fib,frb,aau
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
singletest = ett
secondtester = sgp
while 1:
    day = datetime.today().strftime('%Y-%m-%d')
    tim = datetime.today().strftime('%H:%M')
    deltaT = td.Timedelta()
    #myrep = s.get(url+f"multiArrivalBoard?idList="+vdb.downcode+"|"+vdb.upcode+"|"+vfw.downcode+"|"+vfw.upcode+"|"+hld.downcode+"|"+hld.upcode+"|"+avs.downcode+"|"+avs.upcode+"|"+jag.downcode+"|"+jag.upcode+"|"+nyt.downcode+"|"+nyt.upcode+"|"+aas.downcode+"|"+aas.upcode+"|"+jlg.downcode+"|"+jlg.upcode+"|"+kld.downcode+"|"+kld.upcode+"|"+ett.downcode+"|"+ett.upcode+"|"+sgp.downcode+"|"+sgp.upcode+"|"+dal.downcode+"|"+dal.upcode+"|"+glt.downcode+"|"+glt.upcode+"|"+sbs.downcode+"|"+sbs.upcode+"|"+plp.downcode+"|"+plp.upcode+"|"+gnt.downcode+"|"+gnt.upcode+"|"+ptp.downcode+"|"+ptp.upcode+"|"+fib.downcode+"|"+fib.upcode+"|"+frb.downcode+"|"+frb.upcode+"|"+aau.downcode+"|"+aau.upcode+f"&date="+day+f"&time="+tim+"&duration=30")
    myrep = s.get(url+f"multiArrivalBoard?idList="+singletest.downcode+"|"+singletest.upcode+"|"+secondtester.upcode+"|"+secondtester.downcode+f"&date="+day+f"&time="+tim+"&duration=30")
    #fdict=myrep.json()
    #ettBoard = fdict["Arrival"]

    pp = pprint.PrettyPrinter(depth=4)
    pp.pprint(myrep)

    i = 0

    #twoUp,twoDown = updownTime(ettBoard,singletest,bybus2,i,tim,deltaT)

    #print ("\r" + f"Next 2 towards stop from south is in " + twoUp + f" minutes and the next 2 towards stop from north is in " + twoDown + f" minutes" + "        ", end='')
    time.sleep(60)


   

