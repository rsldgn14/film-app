import requests
from bs4 import BeautifulSoup
from utils.tool import unique

def get_comment(movie_id):
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    url = f"https://www.imdb.com/title/{movie_id}/reviews?ref=tt_ovrt"
    get = requests.get(url, headers=header)
    content = get.content
    soup = BeautifulSoup(content, "html.parser")
    rows = soup.find("div", class_="lister-list").find_all("div")
    all_data = []
    for row in rows:
        temp = row.find("a", class_="title")
        if temp:
            price = temp.text.strip()
            all_data.append(price)
    return unique(all_data)