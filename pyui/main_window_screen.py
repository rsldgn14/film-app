from PyQt5.QtWidgets import QWidget, QMainWindow
from api import api
from api.api import getMovieByTitle

from ui.mainWindow import Ui_MainWindow


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(self.film_ekle)

    def film_ekle(self):
        movie = self.ui.searchInput.text()
        print(movie)
