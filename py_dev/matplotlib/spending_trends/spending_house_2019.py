import matplotlib.pyplot as plt
import csv

x_months = []
y1_internet = []
y2_electric =[]
y3_gas = []
y4_water = []
y5_total = []
y6_split = []

with open('csv_test_2019.csv', 'r') as csvfile:

    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        x_months.append((str(row[0])[:3]))
        y1_internet.append(float((row[1])))
        y2_electric.append((float(row[2])))
        y3_gas.append((float(row[3])))
        y4_water.append((float(row[4])))
        y5_total.append((float(row[5])))
        y6_split.append((float(row[6])))

#Plot of all expenses on same subplot
"""
plt.figure(1)
plt.suptitle('Monthly House Costs')
plt.plot(x_months, y1_internet, 'rs', x_months, y2_electric, 'bo', x_months, y3_gas, 'g^', x_months, y4_water)
"""


plt.figure(2, figsize=(15, 8))
#Graph of monthly electricity cost
plt.subplot(221)
plt.bar(x_months, y2_electric, color='r')
plt.ylim(0,max(y5_total))
plt.title('Electricity')

#Graph of monthly gas cost
plt.subplot(222)
plt.bar(x_months, y3_gas, color='g')
plt.ylim(0,max(y5_total))
plt.title('Gas')

#Graph of monthly water cost
plt.subplot(223)
plt.bar(x_months, y4_water, color='y')
plt.ylim(0,max(y5_total))
plt.title('Water')

#Graph of total monthly cost
plt.subplot(224)
plt.bar(x_months, y5_total)
plt.ylim(0,max(y5_total))
plt.title('Total')

plt.ylabel('Cost')
plt.xlabel('Months')


plt.show()

