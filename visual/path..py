import matplotlib.pyplot as plt
def coordinate():
    x = input("Enter an x value\n")
    y = input ("Enter a y value\n")

    return x, y

def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for count in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return [x_values, y_values]

def run():
    values = path()
    plt.plot(values[0], values[1], 'ro--')

    plt.show()

run()

