from move import Mover,All_agent
import  numpy as np
from field import Field
import matplotlib.pyplot as plt

x_max = 100
y_max = 100
n= 20
# agent = Mover(x_max,y_max)
agent = All_agent(n,x_max,y_max)
# filed = Field(x_max,y_max)
plt.xlim([0,x_max])
plt.ylim([0,y_max])
ax = plt.subplot2grid((1, 1), (0, 0))
x=[]
y=[]
for i in agent.position:
    x.append(i[0])
    y.append(i[1])
lines, = ax.plot(x,y,'.')
# plt.xlim([0,x_max])
# plt.ylim([0,y_max])

# plt.show()
def pause_plot():
    while True:
        agent.move()
        x = []
        y = []
        for i in agent.position:
            x.append(i[0])
            y.append(i[1])
        # print(x,y)
        lines.set_data(x,y)
        ax.set_xlim([0, x_max])
        ax.set_ylim([0, x_max])
        # 一番のポイント
        # - plt.show() ブロッキングされてリアルタイムに描写できない
        # - plt.ion() + plt.draw() グラフウインドウが固まってプログラムが止まるから使えない
        # ----> plt.pause(interval) これを使う!!! 引数はsleep時間
        plt.pause(0.05)
        # plt.draw()
if __name__ == "__main__":
    pause_plot()