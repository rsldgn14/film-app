# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/mresu/OneDrive/Masaüstü/Odev Git/film-app/ui/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 881)
        MainWindow.setMinimumSize(QtCore.QSize(1095, 881))
        MainWindow.setMaximumSize(QtCore.QSize(1095, 881))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(40, 20, 1051, 801))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_2.setMaximumSize(QtCore.QSize(388, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(94,45,132,0.6);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.searchInput.setMaximumSize(QtCore.QSize(286, 22))
        self.searchInput.setText("")
        self.searchInput.setObjectName("searchInput")
        self.horizontalLayout_3.addWidget(self.searchInput)
        self.searchButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.searchButton.setMaximumSize(QtCore.QSize(93, 28))
        self.searchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchButton.setStyleSheet("")
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_3.addWidget(self.searchButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.filmList = QtWidgets.QListWidget(self.horizontalLayoutWidget_7)
        self.filmList.setMaximumSize(QtCore.QSize(388, 720))
        self.filmList.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filmList.setStyleSheet("background-color:rgba(134,204,224,255)\n"
"")
        self.filmList.setWordWrap(True)
        self.filmList.setObjectName("filmList")
        self.verticalLayout.addWidget(self.filmList)
        self.horizontalLayout_11.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label.setMaximumSize(QtCore.QSize(253, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(94,45,132,0.6);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.imageContainer = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.imageContainer.setMinimumSize(QtCore.QSize(0, 250))
        self.imageContainer.setMaximumSize(QtCore.QSize(253, 250))
        self.imageContainer.setStyleSheet("background-color:white;\n"
"border:1px solid;")
        self.imageContainer.setText("")
        self.imageContainer.setAlignment(QtCore.Qt.AlignCenter)
        self.imageContainer.setObjectName("imageContainer")
        self.verticalLayout_2.addWidget(self.imageContainer)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.moviNameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.moviNameLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.moviNameLabel.setObjectName("moviNameLabel")
        self.horizontalLayout_6.addWidget(self.moviNameLabel)
        self.moviNameText = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.moviNameText.setMaximumSize(QtCore.QSize(164, 16))
        self.moviNameText.setText("")
        self.moviNameText.setWordWrap(True)
        self.moviNameText.setObjectName("moviNameText")
        self.horizontalLayout_6.addWidget(self.moviNameText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.yearLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.yearLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.yearLabel.setObjectName("yearLabel")
        self.horizontalLayout_12.addWidget(self.yearLabel)
        self.yearText = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.yearText.setText("")
        self.yearText.setObjectName("yearText")
        self.horizontalLayout_12.addWidget(self.yearText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.rateLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.rateLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.rateLabel.setObjectName("rateLabel")
        self.horizontalLayout_9.addWidget(self.rateLabel)
        self.rateText = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.rateText.setText("")
        self.rateText.setObjectName("rateText")
        self.horizontalLayout_9.addWidget(self.rateText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.csvButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.csvButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.csvButton.setObjectName("csvButton")
        self.verticalLayout_2.addWidget(self.csvButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setMaximumSize(QtCore.QSize(388, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(94,45,132,0.6);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.commentList = QtWidgets.QListWidget(self.horizontalLayoutWidget_7)
        self.commentList.setMaximumSize(QtCore.QSize(388, 757))
        self.commentList.setStyleSheet("background-color:rgba(251,231,180,255);")
        self.commentList.setWordWrap(True)
        self.commentList.setObjectName("commentList")
        self.verticalLayout_3.addWidget(self.commentList)
        self.horizontalLayout_11.addLayout(self.verticalLayout_3)
        self.directorText_2 = QtWidgets.QLabel(self.centralwidget)
        self.directorText_2.setGeometry(QtCore.QRect(810, 680, 274, 16))
        self.directorText_2.setText("")
        self.directorText_2.setObjectName("directorText_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Film-App"))
        self.label_2.setText(_translate("MainWindow", "Search Movie"))
        self.searchButton.setText(_translate("MainWindow", " Search 🔍︎ "))
        self.label.setText(_translate("MainWindow", "Movie Information"))
        self.moviNameLabel.setText(_translate("MainWindow", "Movie Name:"))
        self.yearLabel.setText(_translate("MainWindow", "Year:"))
        self.rateLabel.setText(_translate("MainWindow", "Rate:"))
        self.csvButton.setText(_translate("MainWindow", "Export CSV"))
        self.label_3.setText(_translate("MainWindow", "Comments And Rates"))

