from api.api import getMovieByTitle
from imdbCrawling.web_crawling import get_comment


def get_content(movie):
    res = getMovieByTitle(movie)
    res = res["result"]
    content = []
    for i in range(0, len(res)):
        content.append({"title": res[i]["Title"],
                        "year": res[i]["Year"],
                        "comment": get_comment(res[i]["imdbID"]),
                        "poster": res[i]["Poster"]
                        })
    return content
