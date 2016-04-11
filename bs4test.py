from bs4 import BeautifulSoup

a = BeautifulSoup(open('googleResult.txt'), "html.parser")

print(a.prettify())