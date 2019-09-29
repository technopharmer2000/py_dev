import requests
from bs4 import BeautifulSoup

city_data = requests.get('https://www.zip-codes.com/county/oh-cuyahoga.asp')
#property_data = requests.get()
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

print(city_zip)

