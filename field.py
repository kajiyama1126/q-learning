import numpy as np
import matplotlib.pyplot as plt

class Field(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.field = np.zeros(x,y)

    def mapping(self,position):
        x = position[0]
        y = position[1]
        self.field[x][y] = 1

    def initialize(self):
        self.field = np.zeros(self.x, self.y)
