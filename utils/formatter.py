from api.api import getMovieByTitle

def getContent(movie):
    res = getMovieByTitle(movie)
    res = res["result"]
    content = []

    for i in range(0, len(res)):
        content.append({"title": res[i]["Title"]})
