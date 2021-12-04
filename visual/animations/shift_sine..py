import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()
line = None

def animate(frames):
    global ax
    ax.cla()
    ax.set_xlim(0, 720)
    ax.set_ylim(-1, 1)
    x = range(0, 720)
    y = [math.sin(math.radians(value) + (frames * 0.1)) for value in x]
    print('x:   ', x, 'y: ', y)
    ax.plot(x, y, "ro--")
    plt.show()
    return 0

def run():
    global fig
    my_animation = animation.FuncAnimation(fig, animate, interval=100, frames=720, repeat=False)
    plt.show()


run()  # This is a function call. we call the run function defined above