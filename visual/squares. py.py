import matplotlib.pyplot as plt

def small():
    x = [3, 3, 4, 4, 3]
    y = [3, 4, 4, 3, 3]
    plt.plot(x, y, 'r-o')

def medium():
    x = [2, 2, 5, 5, 2]
    y = [2, 5, 5, 2, 2]
    plt.plot(x, y, 'g-o')

def large():
    x = [1, 6, 6, 1, 1]
    y= [6, 6, 1, 1, 6]
    plt.plot(x, y, 'b-s')

def run():
    small()
    medium()
    large()
    plt.show()
run()