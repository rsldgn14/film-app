import http

import requests


def getMovieByTitle(movie_name):
    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
        'content-type': "application/json",
        'authorization': "apikey 5pWpfXTRw5xZrlq8cjR3zT:5RqnoOUDpWOuusOCLfFeuW"
    }
    conn.request("GET", f"/imdb/imdbSearchByName?query={movie_name}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    return data
