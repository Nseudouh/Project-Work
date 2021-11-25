import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(frame):
    print("frames", frame)
    ax.plot(frame, frame , "ro")


fig, ax = plt.subplots()


def run():
    global fig
    my_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000, repeat=False)
    plt.show()

run()

