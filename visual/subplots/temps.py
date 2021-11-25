import matplotlib.pyplot as plt
# def read_data(file_path):
#     temps= []
#     with open(file_path)as file:
#         for lines in file:
#             temps.append(float(lines.strip()))
#     print(temps)
#     return temps
#
# def run():
#     data = read_data("temps.txt")
#     X_values = range(0,7)
#     fig, (axs1, axs2) = plt.subplots(1, 2)
#     axs1.plot(X_values,data)
#     axs2.bar(X_values, data)
#     plt.show()
#
# run()

import csv
def read_data():
    with open("temps.csv") as csv_file:
        csv_reader= (csv.reader(csv_file))
        lines = next(csv_reader)
        weeks = [week.strip() for week in lines]
        data = {weeks[0]:[], weeks[1]: []}
        for values in csv_reader:
            data[weeks[0]].append(float(values[0].strip()))
            data[weeks[2]].append(float(values[1].strip()))


    return data

def run():
    data = read_data()
    fig, (axs1, axs2) = plt. subplots(1, 2)
    axs1.plot(range(len(data )))












