import matplotlib.pyplot as plt
import csv
import os

x_months = []
y1_internet = []
y2_electric =[]
y3_gas = []
y4_water = []

with open('csv_test.csv', 'r') as csvfile:

    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x_months.append((row[0]))
        y1_internet.append((row[1]))


print (x_months,y1_internet)
"""plt.plot(x_months,y1_internet)
plt.ylabel('Cost')
plt.xlabel('Months')
plt.show()"""