import http
import urllib
import json
import requests


def getMovieByTitle(movie_name):
    parsed_movie_name = urllib.parse.quote(movie_name)
    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
        'content-type': "application/json",
        'authorization': "apikey 5pWpfXTRw5xZrlq8cjR3zT:5RqnoOUDpWOuusOCLfFeuW"
    }
    conn.request("GET", f"/imdb/imdbSearchByName?query={parsed_movie_name}", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    movie_data = json.loads(data)
    return movie_data
