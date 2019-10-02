import csv

with open('tax_rates.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    with open('city_tax.csv', 'w') as city_tax:
        csv_writer = csv.writer(city_tax, delimiter = '\t')

        for row in readCSV:
            tax_rate = row[0][88:100].strip()
            city = row[0][:24].strip()
            csv_writer.writerow((city, tax_rate))
