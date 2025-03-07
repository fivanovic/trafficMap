import numpy as np
import sys
from datetime import datetime
import timedelta as td
import time

class Line:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    lineName = ""

class Station:
    def __init__(self,id,name):
        self.id = id
        self.name = name 
    downcode = ""
    upcode = ""
    name = ""
    upname = ""
    upname2 = ""
    downname = ""
    bottomEndFlag = 0
    topEndFlag = 0

def updownTime(board,stop,bus,i,curtim,delT):
    #print("got it " + stop.name)

    if stop.bottomEndFlag == 1:
        nextUp = "N/A"
    else:
        print("looking for up!")
        for x in board:
            if((board[i]["origin"].startswith(stop.upname))or(board[i]["origin"].startswith(stop.upname2)) and (board[i]["stop"] == stop.name)):
                print("investigating!")
                upArrN = board[i]["name"]
                upArrT = board[i]["time"]
                upArrT = datetime.strptime(upArrT,'%H:%M:%S')
                if upArrN == bus.lineName:
                    print("name match!")
                    arrD = td.Timedelta(upArrT - datetime.strptime(curtim,'%H:%M'))
                    if arrD >= delT:
                        print("time valid!")
                        #print("ping 1!")
                        nextUp = str(arrD.total.minutes)
                        print("heres the next up!" + nextUp)
                        break
                    else:
                        i = i+1
                        continue
                else:
                    i = i+1
                    continue 
            else:
                i = i+1
                continue

    i = 0

    if stop.topEndFlag == 1:
        nextDown = "N/A"
    else:
        for x in board:
            print("looking for down!")
            if(board[i]["origin"].startswith(stop.downname) and (board[i]["stop"] == stop.name)):
                downArrN = board[i]["name"]
                downArrT = board[i]["time"]
                downArrT = datetime.strptime(downArrT,'%H:%M:%S')
                if downArrN == bus.lineName:
                    arrD = td.Timedelta(downArrT - datetime.strptime(curtim,'%H:%M'))
                    if arrD >= delT:
                       #print("ping 2!")
                        nextDown = str(arrD.total.minutes)
                        print("heres the next down!" + nextDown)
                        break
                    else:
                        i = i+1
                        continue
                else:
                    i = i+1
                    continue
            else: 
                i = i+1
                continue
    i = 0

    return nextUp, nextDown
        

