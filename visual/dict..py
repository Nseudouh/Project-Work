import random

import matplotlib.pyplot as plt

def data():
    paths = {}
    line_style = input("what kind of line would you like  ( :, -- or -) ?\n")
    colour_style = input("what kind of colour would you like  ( r, g or ^ ) ?\n")
    marker_style = input ("what style of marker would you like  (o, s or ^) ?\n")

    paths['linestyle'] = line_style
    paths['color'] = colour_style
    paths['marker'] = marker_style


    return paths

def generate ():
    print("How many lines will you like to display? ")
    num_lines = int(input())
    for num_line in range(num_lines):
        values = data()
        x = random.sample(range(1, 10), 5)
        y = random.sample(range(1, 10), 5)
        # format = {'color': values['color'], 'marker': values['marker'], 'linestyle': values['linestyle']}

    plt.plot(x, y, color=values['color'], linestyle=values['linestyle'], marker=values['marker'])
    plt.plot(x, y, format)
    plt.show()

def run():
    print("Drawing ....")
    generate()
    print("Done !")

run()



