import matplotlib.pyplot as plt
import csv
import os


with open('csv_test.csv', 'r') as csvfile:
    x = []
    y = []

    plots = csv.reader(csvfile, delimiter=',')
    lines = csvfile.readlines()
    print (lines[0])
    """def num_y_vars():
        n = 1
        for i in plots[colunm]

    for row in plot:
        x.append([0]))
        y.append(int(row[1]))

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()"""