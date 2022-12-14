import json
import urllib

import requests
import urllib3.util
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow
from api.api import getMovieByTitle
from utils.utils import unique
from ui.mainWindow import Ui_MainWindow


class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.movie_informations = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(self.film_ekle)
        self.ui.filmList.clicked.connect(self.film_getir)

    def film_ekle(self):
        self.ui.filmList.clear()
        movie = self.ui.searchInput.text()
        res = getMovieByTitle(movie)
        self.movie_informations = res["result"]
        unique(self.movie_informations)
        for mov in self.movie_informations:
            self.ui.filmList.addItem(mov["Title"])

    def film_getir(self):
        row = int(self.ui.filmList.currentRow())
        if self.movie_informations[row]["Title"]:
            movie_name = self.movie_informations[row]["Title"]
            self.ui.moviNameText.setText(str(movie_name))
        if self.movie_informations[row]["Poster"]:
            try:
                photo = self.movie_informations[row]["Poster"]
                img = QImage()
                img.loadFromData(requests.get(photo).content)
                self.ui.imageContainer.setPixmap(QPixmap(img))
                self.ui.imageContainer.setScaledContents(True)
            except:
                print("Fatal error")
                self.ui.imageContainer.setText("No Poster")
        if self.movie_informations[row]["Year"]:
            date = self.movie_informations[row]["Year"]
            self.ui.yearText.setText(str(date))
