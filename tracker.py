import numpy as np
import sys

import curses
import time
np.set_printoptions(threshold=sys.maxsize)

L2stat = np.array([" VDB", " HLD", " AVS", " JAG", "NYT ", "AAS ", " JLG", "KLD ", "ETT ", "SGP ", "DAL ", " GLT", " SBS", " PLP", " GNT", " PTP", " FIB", " FRB", " AAU"],dtype=object)
L2split1 = ["SML", "HPT"]
L2dir = np.array([0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,4])
L2NameLoc = np.array([0,0,0,1,3,3,0,2,3,3,3,0,0,0,0,0,0,0,0])

L2Map = np.zeros([55,106],dtype=(str,1))

def writer(labels,names,map, i, j, k):
    temp = list(names[k])

    if labels[k] == 0:
        j = j+1
        map[j,i] = temp[0]
        j = j+1
        map[j,i] = temp[1]
        j = j+1
        map[j,i] = temp[2]
        j = j+1
        map[j,i] = temp[3]
    if labels[k] == 1:
        i = i+1
        map[j,i] = temp[0]
        i = i+1
        map[j,i] = temp[1]
        i = i+1
        map[j,i] = temp[2]
        i = i+1
        map[j,i] = temp[3]
    if labels[k] == 2:
        j = j-1
        map[j,i] = temp[3]
        j = j-1
        map[j,i] = temp[2]
        j = j-1
        map[j,i] = temp[1]
        j = j-1
        map[j,i] = temp[0]
    if labels[k] == 3:
        i = i-1
        map[j,i] = temp[3]
        i = i-1
        map[j,i] = temp[2]
        i = i-1
        map[j,i] = temp[1]
        i = i-1
        map[j,i] = temp[0]
    return

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
        
def draw(map,nameLoc,stat,dir,statNum):
    i = 1
    j = 1
    p = 0
    while p < statNum:
        map[j,i] = "O"
        writer(nameLoc,stat,map,i,j,p)
        lin = lines(map, dir,i,j,p)
        i = lin[0] 
        j = lin[1]
        map[j,i] = "O"
        p = p+1
    return map

L2Map = draw(L2Map,L2NameLoc,L2stat,L2dir,19)

mywindow = curses.initscr()
curses.resize_term( 1000, 1000 )
matrix = L2Map

def flasher(window,s):
    if s == 0:
        window.addstr(1,0,"0")
        s = 1
        return s
    elif s == 1:
        window.addstr(1,0,"O")
        s = 0
        return s
    

def updateMatrix(m):

        return m

def mapmaker(window,map,xoff,yoff):
    i = 0
    j = 0
    while j<55:
        while i<106:
            window.addstr(j+yoff,i+xoff,map[j,i])
            i = i+1
        i = 0
        j = j+1

z = 10
mywindow.addstr("Aalborg Line 2 Visualiser")
s = 0
while z > 1:
    s = flasher(mywindow,s)
    matrix = updateMatrix(matrix)
    try:
        mapmaker(mywindow,L2Map,2,0)
    except curses.error:
        pass
    mywindow.refresh()

    time.sleep(1)

curses.endwin()
quit()
