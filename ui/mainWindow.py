# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/EGE/Downloads/mainWindow.ui'
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
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(30, 30, 1051, 801))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.searchInput.setText("")
        self.searchInput.setObjectName("searchInput")
        self.horizontalLayout_3.addWidget(self.searchInput)
        self.searchButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.searchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_3.addWidget(self.searchButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.filmList = QtWidgets.QListWidget(self.horizontalLayoutWidget_7)
        self.filmList.setStyleSheet("")
        self.filmList.setObjectName("filmList")
        self.verticalLayout.addWidget(self.filmList)
        self.horizontalLayout_11.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.imageContainer = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.imageContainer.setMinimumSize(QtCore.QSize(0, 250))
        self.imageContainer.setStyleSheet("background-color:white;\n"
"border:1px solid;")
        self.imageContainer.setText("")
        self.imageContainer.setObjectName("imageContainer")
        self.verticalLayout_2.addWidget(self.imageContainer)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.moviNameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.moviNameLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.moviNameLabel.setObjectName("moviNameLabel")
        self.horizontalLayout_6.addWidget(self.moviNameLabel)
        self.moviNameText = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.moviNameText.setText("")
        self.moviNameText.setObjectName("moviNameText")
        self.horizontalLayout_6.addWidget(self.moviNameText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.categoryLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.categoryLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.categoryLabel.setObjectName("categoryLabel")
        self.horizontalLayout_7.addWidget(self.categoryLabel)
        self.categoryText = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.categoryText.setText("")
        self.categoryText.setObjectName("categoryText")
        self.horizontalLayout_7.addWidget(self.categoryText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.directorLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.directorLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.directorLabel.setObjectName("directorLabel")
        self.horizontalLayout_8.addWidget(self.directorLabel)
        self.directorText = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.directorText.setText("")
        self.directorText.setObjectName("directorText")
        self.horizontalLayout_8.addWidget(self.directorText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
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
        self.reviewLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.reviewLabel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.reviewLabel.setObjectName("reviewLabel")
        self.horizontalLayout_10.addWidget(self.reviewLabel)
        self.reviewText = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        self.reviewText.setMinimumSize(QtCore.QSize(0, 150))
        self.reviewText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.reviewText.setAutoFillBackground(False)
        self.reviewText.setText("")
        self.reviewText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.reviewText.setObjectName("reviewText")
        self.horizontalLayout_10.addWidget(self.reviewText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.commentList = QtWidgets.QListWidget(self.horizontalLayoutWidget_7)
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
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Movie Information"))
        self.moviNameLabel.setText(_translate("MainWindow", "Movie Name:"))
        self.categoryLabel.setText(_translate("MainWindow", "Category:"))
        self.directorLabel.setText(_translate("MainWindow", "Director:"))
        self.yearLabel.setText(_translate("MainWindow", "Year:"))
        self.rateLabel.setText(_translate("MainWindow", "Rate:"))
        self.reviewLabel.setText(_translate("MainWindow", "Review"))
        self.label_3.setText(_translate("MainWindow", "Comments And Rates"))

