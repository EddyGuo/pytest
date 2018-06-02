import matplotlib.pyplot as plt
from pymatplotlib.random_walk import RandomWalk

# 只要程序处于活跃状态，就不断地模拟随机漫步
keep_running = 'y'

while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    if keep_running == 'n':
        break
    elif keep_running == 'y':
        rw = RandomWalk()
        rw.fill_walk()

        point_numbers = list(range(rw.num_points))
        plt.figure(dpi=128, figsize=(10, 6))
        plt.plot(rw.x_values, rw.y_values, linewidth=1)
        plt.scatter(0, 0, c='green', edgecolors='none', s=60)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=60)

        # 隐藏坐标轴
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)

        plt.show()
        keep_running = input("Make another walk?(y/n)")
    else:
        keep_running = input("Make another walk?(y/n)")
