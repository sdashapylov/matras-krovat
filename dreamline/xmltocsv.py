from bs4 import BeautifulSoup
import csv

file = open('dreamline/stories-everest.xml', 'r')
items = []

def collect_data():
    soup = BeautifulSoup(file, 'lxml')
    offers = soup.find_all('offer')

    for offer in offers:
        type = offer.find('typeprefix').text
        name = offer.find('nameclear').text
        size = offer.find('sizefull').text
        sku = offer.find('vendorcode').text
        items.append([type, name, size, sku])

    return items

collect_data()

myFile = open('dreamline.csv', 'w')
with myFile:
    writer = csv.writer(myFile, delimiter=';')
    writer.writerows(items)

print("Преобразование завершено")