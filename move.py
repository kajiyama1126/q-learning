import numpy as np
import random

class Mover(object):
    def __init__(self,x_max,y_max):
        self.x_max = x_max
        self.y_max = y_max

        wall0_y =[[0,i] for i in range(self.y_max+1)]
        wallxmax_y =[[self.x_max,i] for i in range(self.y_max+1)]
        wallx_0 = [[i, 0] for i in range(self.x_max+1)]
        wallx_ymax = [[i, self.y_max] for i in range(self.x_max+1)]
        self.walls = wall0_y + wallxmax_y + wallx_0 + wallx_ymax

        self.position = self.set_position()

    def set_position(self):
        self.obstract = self.get_obstract()
        while True:
            # position = np.random.randint(low=1,high=10,size=2)
            position_x = random.randint(1,self.x_max-1)
            position_y = random.randint(1, self.y_max - 1)
            position = np.array([position_x,position_y])
            if position.tolist() not in self.obstract:
                return position

    def move(self):
        self.obstract = self.get_obstract()
        while True:
            move = np.random.randint(low=-1,high=2,size=2)
            if (self.position + move).tolist() not in self.obstract:
                self.position = self.position + move
                break

    def get_obstract(self):
        return self.walls



class Multi_Mover(object):
    def __init__(self,x_max,y_max,positon):
        self.x_max = x_max
        self.y_max = y_max

        wall0_y =[[0,i] for i in range(self.y_max+1)]
        wallxmax_y =[[self.x_max,i] for i in range(self.y_max+1)]
        wallx_0 = [[i, 0] for i in range(self.x_max+1)]
        wallx_ymax = [[i, self.y_max] for i in range(self.x_max+1)]
        self.walls = wall0_y + wallxmax_y + wallx_0 + wallx_ymax

        self.position = self.set_position(positon)

    def set_position(self,position):
        self.obstract = self.get_obstract(position)
        while True:
            # position = np.random.randint(low=1,high=10,size=2)
            position_x = random.randint(1,self.x_max-1)
            position_y = random.randint(1, self.y_max - 1)
            position = np.array([position_x,position_y])
            if position.tolist() not in self.obstract:
                return position

    def move(self,position):
        self.obstract = self.get_obstract(position)
        while True:
            move = np.random.randint(low=-1,high=2,size=2)
            if (self.position + move).tolist() not in self.obstract:
                self.position = self.position + move
                break

    def get_obstract(self,position):
        return self.walls + position


class All_agent(object):
    def __init__(self,n,x_max,y_max):
        self.allagent = []
        self.position = []
        self.n = n
        for i in range(self.n):
            agent = Multi_Mover(x_max,y_max,self.position)
            self.position.append(agent.position.tolist())
            self.allagent.append(agent)


    def move(self):
        for i in range(self.n):
            self.allagent[i].move(self.position)
            self.position[i] = self.allagent[i].position.tolist()
