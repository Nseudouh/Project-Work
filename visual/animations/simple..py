import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

def animate(frame):
    global ax
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ax.plot(x[:frame], y[:frame], "ro--")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)





def run():
    global fig
    my_animation = animation.FuncAnimation(fig, animate, interval=1000, frames=10,repeat=False,)
    plt.show()


run()