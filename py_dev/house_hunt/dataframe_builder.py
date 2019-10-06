import requests
from bs4 import BeautifulSoup
import json
import re
from selenium import webdriver
import pandas as pd
import itertools
import matplotlib.pyplot as plt

#mortgage/loan data
loan_data = {
    'interest_rate' : 0.036,
    'funding_fee' : 0.022,
    'closing_costs' : 0.035
}


#monthly fixed epense calc variables
fixed_expenses = {
    'water_sewer' : 150,
    'electric_gas' : 85
    }


with open('house_data.json', 'r') as hd:
    hd = json.load(hd)

    address = []
    price = []
    beds = []
    baths = []
    units = []
    rent_data = []
    tax_rate = []
    principle = []
    interest = []
    funding_fee = []
    property_tax = []
    monthly_fixed_expense = []


    for house in hd:

        address.append(house['address'])
        price.append(house['price'])
        beds.append(house['beds'])
        baths.append(house['baths'])
        units.append(house['units'])
        rent_data.append(house['rent_data'])
        tax_rate.append(house['tax_rate'])
        p = round(float(int(house['price']) / (30 * 12)),2)
        principle.append(p)
        i = round(float((int(house['price']) * float(loan_data['interest_rate'])) / (30 * 12)),2)
        interest.append(i)
        f = round(float((int(house['price']) * float(loan_data['funding_fee'])) / (30 * 12)),2)
        funding_fee.append(f)
        t = round(float(int(house['price']) * float(house['tax_rate']) / 12),2)
        property_tax.append(t)
        monthly_fixed_expense.append(p+i+f+t+fixed_expenses['water_sewer']+fixed_expenses['electric_gas'])

    #print (list(x[0]['unit1'] for x in rent_data))


    for a, p, fe, rd in zip(address, price, monthly_fixed_expense, list(x[0]['unit1'] for x in rent_data)):
        print (a + ' | ' + p)
        print (str(fe) + ' | ' + str(round(float(rd)-float(fe), 2)))






    """
    cols = ['Address',
            'Price',
            'Beds',
            'Baths',
            'Units',
            'Rent Data',
            'Tax Rate',
            principle = []
            interest = []
            funding_fee = []
            property_tax = []
            monthly_fixed_expense = []
            ]

    lisboa = pd.DataFrame({'Address': address,
                           'Price': price,
                           'Beds': beds,
                           'Baths': baths,
                           'Units': units,
                           'Rent Data': rent_data,
                           'Tax Rate': tax_rate})[cols]

    lisboa.to_excel('lisboa_raw.xls')
"""