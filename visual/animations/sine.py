import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


fig, ax = plt.subplots()

def animate(frame):
    global ax
    ax.set_xlim(0, 720), ax.set_ylim(-1, 1)
    x = range(frame)
    y = [math.sin(math.radians(value)) for value in x]
    ax.plot(x, y, "ro--")

def run():
    global fig
    my_animation = animation.FuncAnimation(fig, animate, frames=720, interval=100, repeat=False)
    plt.show()

run()