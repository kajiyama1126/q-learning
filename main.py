from move import All_agent,Camera
import  numpy as np
from field import Field
import matplotlib.pyplot as plt
# import seaborn
x_max = 5
y_max = 5
x_range=1
y_range = 1
n= 4
# agent = Mover(x_max,y_max)
agent = All_agent(n,x_max,y_max)
camera = Camera(n,x_max,y_max,x_range,y_range)
# filed = Field(x_max,y_max)
plt.xlim([0,x_max])
plt.ylim([0,y_max])
ax = plt.subplot2grid((1, 1), (0, 0))
x=[]
y=[]
for i in agent.all_position:
    x.append(i[0])
    y.append(i[1])
lines, = ax.plot(x,y,'.')

camera_x = []
camera_y = []
for i in camera.image_outline:
    camera_x.append(i[0])
    camera_y.append(i[1])
camera_lines, = ax.plot(camera_x,camera_y,'-')
# plt.xlim([0,x_max])
# plt.ylim([0,y_max])

# plt.show()

def pause_plot():
    count = 0
    for i in range(10000):
        count += 1
        if count %2 == 0:
            agent.move()
        camera.action_select(agent.all_position,i)
        print(count)
        # print(camera.state_action_value)
        x = []
        y = []
        for i in agent.all_position:
            x.append(i[0])
            y.append(i[1])

        camera_x = []
        camera_y = []
        for i in camera.image_outline:
            camera_x.append(i[0])
            camera_y.append(i[1])

        # print(x,y)
        lines.set_data(x,y)
        camera_lines.set_data(camera_x, camera_y)
        ax.set_xlim([0, x_max])
        ax.set_ylim([0, x_max])
        # 一番のポイント
        # - plt.show() ブロッキングされてリアルタイムに描写できない
        # - plt.ion() + plt.draw() グラフウインドウが固まってプログラムが止まるから使えない
        # ----> plt.pause(interval) これを使う!!! 引数はsleep時間
        plt.pause(0.04)
        # plt.draw()
if __name__ == "__main__":
    pause_plot()