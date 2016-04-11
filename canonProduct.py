productList = []

f = open('product.txt')

lines = f.readlines()

for line in lines:
    productList.append(line.strip())

for p in productList:
    print(p)

def generateSearchURL(product):
    result = product.replace(' ', '+')
    result = result.replace('/', '%2F')
    return result

codedProducts = [generateSearchURL(p) for p in productList]

for p in codedProducts:
    print(p)

import requests
from bs4 import BeautifulSoup

proxies = {
  'http': 'http://127.0.0.1:8787',
  'https': 'http://127.0.0.1:8787'
}

baseURL = 'https://www.google.com/search?q='

productSearchURL = baseURL + codedProducts[0]

print(productSearchURL)

r = requests.get(productSearchURL, proxies=proxies)

print(r.text)

with open("googleResult.txt","a+") as f:
    f.write(r.text)



soup = BeautifulSoup(r.text)

print(soup.text)