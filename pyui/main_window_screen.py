import requests
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow
from utils.formatter import get_content
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
        self.ui.commentList.clear()
        self.ui.reviewText.clear()
        self.ui.imageContainer.clear()
        self.ui.moviNameText.clear()
        self.ui.yearText.clear()
        self.ui.categoryText.clear()
        self.ui.rateText.clear()
        self.ui.directorText_2.clear()
        movie = self.ui.searchInput.text()
        self.movie_informations = get_content(movie)
        for mov in self.movie_informations:
            self.ui.filmList.addItem(mov["title"])

    def film_getir(self):
        row = int(self.ui.filmList.currentRow())

        if self.movie_informations[row]["title"]:
            movie_name = self.movie_informations[row]["title"]
            self.ui.moviNameText.setText(str(movie_name))
        if self.movie_informations[row]["poster"]:
            try:
                photo = self.movie_informations[row]["poster"]
                img = QImage()
                img.loadFromData(requests.get(photo).content)
                self.ui.imageContainer.setPixmap(QPixmap(img))
                self.ui.imageContainer.setScaledContents(True)
            except:
                print("Fatal error")
                self.ui.imageContainer.setText("No Poster")
        if self.movie_informations[row]["year"]:
            date = self.movie_informations[row]["year"]
            self.ui.yearText.setText(str(date))

        if self.movie_informations[row]["comment"]:
            try:
                self.ui.commentList.clear()
                for comment in self.movie_informations[row]["comment"]:
                    self.ui.commentList.addItem(comment)
            except:
                print("no commento")
