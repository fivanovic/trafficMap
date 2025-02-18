import numpy as np
import sys

import curses
import time
numpy.set_printoptions(threshold=sys.maxsize)

L2stat = np.array(["VDB", "HLD", "AVS", "JAG", "NYT", "AAS", "JLG", "KLD", "ETT", "SGP", "DAL", "GLT", "SBS", "PLP", "GNT", "PTP", "FIB", "FRB", "AAU"],dtype=object)
L2split1 = ["SML", "HPT"]
L2dir = np.array([0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,4])
L2NameLoc = np.array([0,0,0,2,3,3,0,2,3,3,3,0,0,0,0,0,0,0,0])

i = 0
j = 0
k = 0
starter = [2,2]
L2Map = np.zeros([55,106],dtype=(str,3))
#print(len(L2stat))
#print(len(L2dir))
#rint(len(L2NameLoc))

#pass stations, direction, and label location 


def writer(labels, i, j, k):
    if labels[k] == 0:
        j = j+1
    if labels[k] == 1:
        i = i+1
    if labels[k] == 2:
        j = j-1
    if labels[k] == 3:
        i = i-1
    return i, j

def lines(map,dir, i, j, k):
    if dir[k] == 0:
        z = 0
        i = i+1
        while z<7:
            map[j,i] = "-"
            z = z+1
            i = i+1
        return i, j
    if dir[k] == 1:
        z = 0
        j = j+1
        while z<7:
            map[j,i] = "|"
            z = z+1
            j = j+1
        return i, j
    if dir[k] == 4:
        
        return i, j
        
        

i = 1
j = 1
p = 0

while p < 19:
    L2Map[j,i] = "O"
    lab = writer(L2NameLoc,i,j,p)
    L2Map[lab[1], lab[0]] = L2stat[p]
    lin = lines(L2Map, L2dir,i,j,p)
    i = lin[0] 
    j = lin[1]
    L2Map[j,i] = "O"
    p = p+1

i = 0
j = 0
"""
while j < 106:
    while i < 19:
        if L2Map[j,i] == 0:
            L2Map[j,i] = " "
        i = i+1
    j = j+1
"""
#print(L2Map)
#np.savetxt("test.csv", L2Map, delimiter=",", fmt='%s')

mywindow = curses.initscr()

matrix = L2Map

def updateMatrix(m):
    if m[0][0] == "I":
        m[0][0] = "i"
        return m
    else:
        m[0][0] = "I"
        return m

def getMarixString(m):
    x = ''
    for row in m:
        x += ' '.join(str(item) for item in row)
        x += "\n"
    return x

z = 10
mywindow.addstr("Aalborg Line 2 Visualiser")
while z > 1:
    matrix = updateMatrix(matrix)
    try:
        mywindow.addstr(1,0, getMarixString(matrix))
    except curses.error:
        pass
    mywindow.refresh()

    time.sleep(1)

curses.endwin()
quit()