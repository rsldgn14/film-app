from bs4 import BeautifulSoup
from utils.tool import unique
import requests


def get_comment(movie_id):
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    url = f"https://www.imdb.com/title/{movie_id}/reviews?ref=tt_ovrt"
    get = requests.get(url, headers=header)
    content = get.content
    soup = BeautifulSoup(content, "html.parser")
    rows = soup.find("div", class_="lister-list").find_all("div", class_="lister-item-content")
    ratings = soup.find("div", class_="lister-list").find_all("span", class_="rating-other-user-rating")
    all_data = []
    rating_array = []
    i = 0
    for rating in ratings:
        rating_temp = rating.find("span", class_="")
        if rating_temp:
            rating = rating_temp.text.strip()
            rating_array.append(rating)

    for row in rows:
        temp = row.find("a", class_="title")
        temp2 = row.find("span", class_="display-name-link")
        if temp:
            comment = temp.text.strip()
            username = temp2.text.strip()
            all_data.append({"comment": comment, "username": username, "rate": rating_array[i]})
            if i < 10:
                i = i + 1
    return all_data


def get_rate(movie_id):
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    url = f"https://www.imdb.com/title/{movie_id}/ratings/?ref_=tt_ov_rt"
    get = requests.get(url, headers=header)
    content = get.content
    soup = BeautifulSoup(content, "html.parser")
    rows = soup.find("span", class_="ipl-rating-star__rating")
    return rows.text.strip()


