import requests

from bs4 import BeautifulSoup

url = "https://www.imdb.com/"

get = requests.get(url)
print(get.status_code)
def getMovieByTitle(searchParam):
    url = "https://imdb8.p.rapidapi.com/title/find"
    querystring = {"q": searchParam}
    headers = {
        "X-RapidAPI-Key": "d19d3d8e07mshc2083cb18c1ab08p1b7266jsn2516f359fd7f",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    title = response.json()
    movies = title["results"]

    return movies
