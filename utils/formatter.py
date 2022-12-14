from api.api import getMovieByTitle
from imdbCrawling.web_crawling import get_comment


def get_content(movie):
    res = getMovieByTitle(movie)
    res = res["result"]
    content = []
    for i in range(0, len(res)):
        content.append({
                        "id": res[i]["imdbID"],
                        "title": res[i]["Title"],
                        "year": res[i]["Year"],
                        "poster": res[i]["Poster"]
                        })
    return content
