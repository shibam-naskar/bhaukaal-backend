import requests
from bs4 import BeautifulSoup

object = requests.get("https://cineb.net")
soup = BeautifulSoup(object.content,"html.parser")

alldata = soup.find_all(class_="flw-item")
for i in alldata:
    ancour = i.find_all('a',{"class": "film-poster-ahref"})
    link = ancour[0].get('href')
    image = i.find_all('img')
    name = i.find_all('a',{"class": "film-poster-ahref"})
    
    print(name[0].get('title'))
    print(f'https://cineb.net{link}')
    print(image[0].get('data-src'))