##Enter any State (in 2 character,lowercase form)
# and any of that State's counties (lowercase, without the word 'county').
##Returns a list of that county's cities and zip codes.

import requests
from bs4 import BeautifulSoup

def get_city_zip():
    state = input('state (2 char): ')
    county = input("county (sans 'county'):")

    url = 'https://www.zip-codes.com/county/{}-{}.asp'.format(state, county)
    city_data = requests.get(url)

    soup = BeautifulSoup(city_data.text, "html.parser")

    table = soup.find('table', {'class': 'statTable'})
    links = table.find_all('a', {'style': 'text-decoration:underline;'})
    city_zip = []
    for link in links:
        title = link.get('title')
        city = title.split()[3].strip(',')
        zip = title.split()[2].strip(',')
        city_zip.append((city, zip))

    print(city_zip)

get_city_zip()