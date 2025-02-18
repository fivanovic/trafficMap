import numpy as np
import sys


class Station:
    def __init__(self,id,name):
        self.id = id
        self.name = name 
    
    arrBoard = np.array([3,4,5,6,7,8,9,10])

    def timemarch(self):
        self.arrBoard = self.arrBoard - 1
        try:
            if self.arrBoard[0] == 0:
                self.arrBoard = self.arrBoard[1:-1]
        except:
            pass

    downcode = ""
    upcode = ""
        

