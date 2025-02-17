import curses
import time

mywindow = curses.initscr()

matrix = [[3,2,3],[1,10,1],[2,8,6]]

def updateMatrix(m):
    if m[1][1] > 0:
        m[1][1] = m[1][1] - 1
        return m
    else:
        m[1][1] = 10
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
    
    mywindow.addstr(1,0, getMarixString(matrix))
    mywindow.refresh()

    time.sleep(1)

curses.endwin()
quit()