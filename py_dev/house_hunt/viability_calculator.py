import requests
from bs4 import BeautifulSoup

city_data = requests.get('https://www.zip-codes.com/county/oh-cuyahoga.asp')
property_data = requests.get(input("Enter the property URL from Realtor.com: "))
#tax_data = requests.get()

city_zip = []
CityTaxRate = []

#get the cities and zip codes
soup = BeautifulSoup(city_data.text, "html.parser")

table = soup.find('table', {'class': 'statTable'})
links = table.find_all('a', {'style': 'text-decoration:underline;'})
for link in links:
    title = link.get('title')
    city = title.split()[3].strip(',')
    zip = title.split()[2].strip(',')
    city_zip.append((city, zip))

#get property data from realtor.com
soup = BeautifulSoup(property_data.text, "html.parser")

#prop_info = soup.find('div', {'class': 'jsx-3586775753 listing-information-cmp'})
price = soup.find('span', {'class': 'jsx-3586775753 price'}).get_text()

print (price)
