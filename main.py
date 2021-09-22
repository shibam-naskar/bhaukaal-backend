from flask import Flask,jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def entry_point():
    return 'Hello This is Bhaulaal Backend'

@app.route('/movies')
def movies():
    homeMovies=[]
    object = requests.get("https://cineb.net")
    soup = BeautifulSoup(object.content,"html.parser")

    alldata = soup.find_all(class_="flw-item")
    for i in range(0,100):
        ancour = alldata[i].find_all('a',{"class": "film-poster-ahref"})
        link = ancour[0].get('href')
        image = alldata[i].find_all('img')
        name = alldata[i].find_all('a',{"class": "film-poster-ahref"})

        if image[0].get('data-src') != None:
        
            homeMovies.append(
                {
                    "name":name[0].get('title'),
                    "movieLink":f'https://cineb.net{link}',
                    "poster":image[0].get('data-src')
                }
            )
    
    response = jsonify(homeMovies)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/search/<string:n>')
def search(n):
    
    a = n.replace(' ','-')
    homeMovies=[]
    object = requests.get(f"https://cineb.net/search/{a}")
    soup = BeautifulSoup(object.content,"html.parser")

    alldata = soup.find_all(class_="flw-item")
    for i in range(0,len(alldata)):
        ancour = alldata[i].find_all('a',{"class": "film-poster-ahref"})
        link = ancour[0].get('href')
        image = alldata[i].find_all('img')
        name = alldata[i].find_all('a',{"class": "film-poster-ahref"})

        if image[0].get('data-src') != None:
        
            homeMovies.append(
                {
                    "name":name[0].get('title'),
                    "movieLink":f'https://cineb.net{link}',
                    "poster":image[0].get('data-src')
                }
            )
    
    response = jsonify(homeMovies)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(debug=True)