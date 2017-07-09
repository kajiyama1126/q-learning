import numpy as np
import random
import copy
# class Mover(object):
#     def __init__(self,x_max,y_max):
#         self.x_max = x_max
#         self.y_max = y_max
#
#         wall0_y =[[0,i] for i in range(self.y_max+1)]
#         wallxmax_y =[[self.x_max,i] for i in range(self.y_max+1)]
#         wallx_0 = [[i, 0] for i in range(self.x_max+1)]
#         wallx_ymax = [[i, self.y_max] for i in range(self.x_max+1)]
#         self.walls = wall0_y + wallxmax_y + wallx_0 + wallx_ymax
#
#         self.position = self.set_position()
#
#     def set_position(self):
#         self.obstract = self.get_obstract()
#         while True:
#             # position = np.random.randint(low=1,high=10,size=2)
#             position_x = random.randint(1,self.x_max-1)
#             position_y = random.randint(1, self.y_max - 1)
#             position = np.array([position_x,position_y])
#             if position.tolist() not in self.obstract:
#                 return position
#
#     def move(self):
#         self.obstract = self.get_obstract()
#         while True:
#             move = np.random.randint(low=-1,high=2,size=2)
#             if (self.position + move).tolist() not in self.obstract:
#                 self.position = self.position + move
#                 break
#
#     def get_obstract(self):
#         return self.walls



class Multi_Mover(object):
    def __init__(self,x_max,y_max,obs_posi):
        self.x_max = x_max
        self.y_max = y_max

        wall0_y =[[0,i] for i in range(self.y_max+1)]
        wallxmax_y =[[self.x_max,i] for i in range(self.y_max+1)]
        wallx_0 = [[i, 0] for i in range(self.x_max+1)]
        wallx_ymax = [[i, self.y_max] for i in range(self.x_max+1)]
        self.walls = wall0_y + wallxmax_y + wallx_0 + wallx_ymax

        self.position = self.set_position(obs_posi)

    def set_position(self,obs_posi):
        self.obstract = self.get_obstract(obs_posi)
        while True:
            # position = np.random.randint(low=1,high=10,size=2)
            position_x = random.randint(1,self.x_max-1)
            position_y = random.randint(1, self.y_max - 1)
            position = np.array([position_x,position_y])
            if position.tolist() not in self.obstract:
                return position

    def move(self,obs_posi):
        self.obstract = self.get_obstract(obs_posi)
        while True:
            move = np.random.randint(low=-1,high=2,size=2)
            if (self.position + move).tolist() not in self.obstract:
                self.position = self.position + move
                break

    def get_obstract(self,obs_posi):
        return self.walls + obs_posi


class All_agent(object):
    def __init__(self,n,x_max,y_max):
        self.allagent = []
        self.all_position = []
        self.n = n
        for i in range(self.n):
            agent = Multi_Mover(x_max,y_max,self.all_position)
            self.all_position.append(agent.position.tolist())
            self.allagent.append(agent)


    def move(self):
        for i in range(self.n):
            self.allagent[i].move(self.all_position)
            self.all_position[i] = self.allagent[i].position.tolist()

class Camera(Multi_Mover):
    def __init__(self,max_people,x_max,y_max,x_range,y_range,obs_posi=[]):
        super(Camera,self).__init__(x_max,y_max,obs_posi)
        self.x_range = x_range
        self.y_range = y_range
        self.image_range = None
        self.image_outline = None
        self.make_image_range()
        self.make_image_outline()
        self.n = max_people
        self.action_pattern = 9
        self.alpha = 0.1
        self.gamma = 0.9
        # print(self.image_range)
        # print(self.image_outline)
        self.state_action_value = np.zeros((self.n,self.x_max,self.y_max,self.action_pattern),dtype=float)
        self.state_action_count = np.ones((self.n, self.x_max, self.y_max, self.action_pattern), dtype=int)
        # print(self.state_pattern)

    def make_image_range(self):
        x= self.position[0]
        y=self.position[1]
        self.image_range =[[x + i,y+j] for i in range(-self.x_range,self.x_range + 1) for j in range(-self.y_range,self.y_range+1)]

    def make_image_outline(self):
        x= self.position[0]
        y= self.position[1]
        # x_outline = [[x+i,j] for j in range(-self.y_range,self.y_range+1) for i in [-self.x_range,self.x_range]]
        # y_outline =  [[i,y+j] for i in range(-self.x_range,self.x_range+1) for j in [-self.y_range,self.y_range]]
        outline1 = [[x+i,y-self.y_range]  for i in [-self.x_range,self.x_range]]
        outline2 = [[x-i,y+self.y_range] for i in [-self.x_range,self.x_range]]
        self.image_outline = outline1+ outline2 + [[x-self.x_range,y-self.y_range]]
    # def action(self):

    def reward(self,position):
        reward = 0
        for i in position:
            if i in self.image_range:
                reward += 1

        return reward

    def count_people(self,position):
        people = 0
        for i in position:
            if i in self.image_range:
                people += 1

        return people

    def learn(self,people,x,y,act,reward,next_people,next_x,next_y):
        Q = copy.copy(self.state_action_value[people-1][x][y][act])
        Q = (1-self.alpha)*Q +self.alpha*(reward + self.gamma*(np.argmax(self.state_action_value[next_people-1][next_x][next_y])))
        self.state_action_value[people-1][x][y][act] = Q

    def random_action(self):
        self.obstract = self.get_obstract(obs_posi=[])
        while True:
            move = np.random.randint(low=-1,high=2,size=2)
            if (self.position + move).tolist() not in self.obstract:
                self.position = self.position + move
                self.make_image_range()
                self.make_image_outline()
                print(self.image_outline)
                break

    def action(self,act):
        if act == 0 :
            move = np.array([-1,-1])
        elif act == 1:
            move = np.array([-1, 0])
        elif act == 2:
            move = np.array([-1, 1])
        elif act == 3:
            move = np.array([0, -1])
        elif act == 4:
            move = np.array([0, 0])
        elif act == 5:
            move = np.array([0, 1])
        elif act == 6:
            move = np.array([1, -1])
        elif act == 7:
            move = np.array([1, 0])
        elif act == 8:
            move = np.array([1, 1])
        # move = np.array([x,y])
        # if (self.position + move).tolist() not in self.obstract:
        self.position = self.position + move

        # print(self.image_outline)
        # break

    def action_select(self,agent_position,count):
        self.obstract = self.get_obstract(obs_posi=[])
        people = self.count_people(agent_position)
        x= self.position[0]
        y= self.position[1]

        while True:
            now_position = self.position
            if random.random() < 0.1:
                act = random.randint(0,self.action_pattern-1)
            else:
                act = np.argmax((self.state_action_value[people-1][x][y])/self.state_action_count[people-1][x][y])
            self.action(act)

            if self.position.tolist() not in self.obstract:
                self.state_action_count[people - 1][x][y][act] += 1
                self.make_image_range()
                self.make_image_outline()

                reward = self.reward(agent_position)
                self.learn(people,now_position[0],now_position[1],act,reward,reward,self.position[0],self.position[1])

                return
            self.position = now_position




