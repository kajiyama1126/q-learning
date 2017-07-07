from move import Mover
import  numpy as np
from field import Field
import matplotlib.pyplot as plt

x_max = 10
y_max = 10
agent = Mover(x_max,y_max)

# filed = Field(x_max,y_max)
plt.xlim([0,x_max])
plt.ylim([0,y_max])
fig, ax = plt.subplots(1, 1)
x = agent.position[0]
y = agent.position[1]
lines = ax.plot(np.array(x),np.array(y))
# plt.xlim([0,x_max])
# plt.ylim([0,y_max])

# plt.show()
def pause_plot():
    while True:
        agent.move()
        x = agent.position[0]
        y = agent.position[1]
        print(x,y)
        lines.set_data(np.array(x),np.array(y))
        ax.xlim([0, x_max])
        # 一番のポイント
        # - plt.show() ブロッキングされてリアルタイムに描写できない
        # - plt.ion() + plt.draw() グラフウインドウが固まってプログラムが止まるから使えない
        # ----> plt.pause(interval) これを使う!!! 引数はsleep時間
        plt.pause(.1)

if __name__ == "__main__":
    pause_plot()