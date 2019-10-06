import requests
from bs4 import BeautifulSoup
import json


##HTML.parse(saved homes) to find request urls and .get(home data)
def get_home_data():
    with open('saved_homes.html', 'r') as f :
        property_data = f.read()

    soup = BeautifulSoup(property_data, "html.parser")

    data = soup.find('script', {'id':'__NEXT_DATA__'})

    url_coontainer = str(data).split('"property_listings":', 1)[1].split(',"extra_data":',1)[0]

    urls =[]

    for url in json.loads(url_coontainer):
        urls.append(url['ldp_url'])

    #print ('\n'.join(urls))

    #create list for all of the houses' data
    house_data = []

    #get each homes data from url in urls:
    for url in urls:
        soup = BeautifulSoup(requests.get(url).text, "html.parser")

        #house data required
        house = {
        'address' : [],
        'price' : [],
        'beds' : [],
        'baths' : [],
        'units' : [],
        'rent_data' : [],
        'tax_rate' : []
        }

        #get house address
        address = soup.find('span', {'itemprop': 'streetAddress'}).text.strip(',')
        house['address'] = address

        print('collecting data: ' + address)

        #get house price
        price = ''.join(filter(lambda x: x.isdigit(), soup.find('span', {'itemprop': 'price'}).text))
        house['price'] = price

        #get number of bedrooms in house
        bed = ''.join(filter(lambda x: x.isdigit(), soup.find('li', {'data-label': 'property-meta-beds'}).text))
        house['beds'] = bed

        #get number of bathrooms in house
        bath = ''.join(filter(lambda x: x.isdigit(), soup.find('li', {'data-label': 'property-meta-bath'}).text))
        house['baths'] = bath

        #get the total number of current units
        num_unit = input("# of units: ")
        house['units'] = num_unit

        #get the current rent for each unit
        rents = []
        for u in range(int(num_unit)):
            rent = input("Unit " + str(u+1) + " rent: ")
            rents.append({str('unit' + str(u+1)) : rent})
        house['rent_data'] = rents

        #get the zip code tax rate
        tax = input("Enter zip code tax rate (ie: 0.023): ")
        house['tax_rate'] = tax

        house_data.append(house)

        print (address + ' appended')

    with open('house_data.json', 'w') as fout:
        json.dump(house_data, fout)

    print (house_data)

get_home_data()


