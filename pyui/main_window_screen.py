import csv

import requests
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow
from utils.formatter import get_content
from ui.mainWindow import Ui_MainWindow
from imdbCrawling.web_crawling import get_comment, get_rate


class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.movie_informations = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(self.film_ekle)
        self.ui.filmList.clicked.connect(self.film_getir)
        self.ui.csvButton.clicked.connect(self.export_csv)

    def film_ekle(self):
        self.ui.filmList.clear()
        self.ui.commentList.clear()
        self.ui.imageContainer.clear()
        self.ui.moviNameText.clear()
        self.ui.yearText.clear()
        self.ui.rateText.clear()
        movie = self.ui.searchInput.text()
        self.movie_informations = get_content(movie)
        for mov in self.movie_informations:
            self.ui.filmList.addItem(mov["title"])
        self.comment_informations = []
        self.row = 0

    def film_getir(self):
        self.ui.commentList.clear()
        self.row = int(self.ui.filmList.currentRow())
        movie_id = self.movie_informations[self.row]["id"]
        if self.movie_informations[self.row]["title"]:
            movie_name = self.movie_informations[self.row]["title"]
            self.ui.moviNameText.setText(str(movie_name))
        if self.movie_informations[self.row]["poster"]:
            try:
                photo = self.movie_informations[self.row]["poster"]
                img = QImage()
                img.loadFromData(requests.get(photo).content)
                self.ui.imageContainer.setPixmap(QPixmap(img))
                self.ui.imageContainer.setScaledContents(True)
            except:
                print("Fatal error")
                self.ui.imageContainer.setText("No Poster")
        if self.movie_informations[self.row]["year"]:
            date = self.movie_informations[self.row]["year"]
            self.ui.yearText.setText(str(date))

        try:
            self.ui.rateText.setText(get_rate(movie_id))
        except:
            self.ui.rateText.setText("No Rate")
        comments = get_comment(movie_id)
        if comments:
            try:
                self.comment_informations = []
                for i in range(len(comments)):
                    self.comment_informations = self.comment_informations + [comments[i]['username'],
                                                                             comments[i]['comment'],
                                                                             comments[i]['rate']]
                    self.ui.commentList.addItem(
                        f"{comments[i]['username']} ----{comments[i]['comment']}----{comments[i]['rate']}")
            except:
                self.comment_informations = []
                print("no commento")

    def export_csv(self):
        movie_id = self.movie_informations[self.row]["id"]
        with open('movies.csv', 'a', newline="\n", encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow([self.movie_informations[self.row]["title"], self.movie_informations[self.row]["year"],
                             get_rate(movie_id), get_comment(movie_id)])
