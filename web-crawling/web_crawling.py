import requests
from bs4 import BeautifulSoup
from utils.utils import unique
from api.api import getMovieByTitle

res = getMovieByTitle("recep ivedik 7")
imdbId = res["result"][0]["imdbID"]

url = f"https://www.imdb.com/title/{imdbId}/reviews?ref=tt_ovrt"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
rows = soup.find("div", _class="lister").find_all("div")
"""all_data = []
for row in rows:
    temp = row.find("a", _class="title")
    if temp:
        price = temp.text.strip()
        all_data.append(price)
print(unique(all_data))"""
print(rows)

