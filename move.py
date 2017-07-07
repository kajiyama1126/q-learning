import numpy as np
import random

class Mover(object):
    def __init__(self,x_max,y_max):
        self.x_max = x_max
        self.y_max = y_max
        self.position = self.set_position()

    def set_position(self):
        x_axis = random.randint(0, self.x_max)
        y_axis = random.randint(0,self.y_max)
        return np.array([x_axis,y_axis])

    def move(self):
        if self.position[0] == self.x_max:
            x_move = random.randint(0, 1) -1
        elif self.position[0] == 0:
            x_move = random.randint(0, 1)
        else:
            x_move = random.randint(0, 2) -1

        if self.position[1] == self.y_max:
            y_move = random.randint(0, 1) -1
        elif self.position[1] == 0:
            y_move = random.randint(0, 1)
        else:
            y_move = random.randint(0, 2) -1

        self.position = self.position + np.array([x_move,y_move])