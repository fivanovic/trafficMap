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

def updownTime(board,stopname,i,upname,upname2,downname,busname,curtim,delT):
    if (board[i]["stop"].startswith(stopname)):
        for x in board:
            if(board[i]["origin"].startswith(upname)) or (board[i]["origin"].startswith(upname2)):
                upArrN = board[i]["name"]
                upArrT = board[i]["time"]
                upArrT = datetime.strptime(upArrT,'%H:%M:%S')
                if upArrN == busname:
                    arrD = td.Timedelta(upArrT - datetime.strptime(curtim,'%H:%M'))
                    if arrD >= delT:
                        nextUp = str(arrD.total.minutes)
                        break
            i = i+1
        i = 0

        for x in board:
            if(board[i]["origin"].startswith(downname)):
                downArrN = board[i]["name"]
                downArrT = board[i]["time"]
                downArrT = datetime.strptime(downArrT,'%H:%M:%S')
                if downArrN == busname:
                    arrD = td.Timedelta(downArrT - datetime.strptime(curtim,'%H:%M'))
                    if arrD >= delT:
                        nextDown = str(arrD.total.minutes)
                        break
            i = i+1
        i = 0
    return nextUp, nextDown
        

