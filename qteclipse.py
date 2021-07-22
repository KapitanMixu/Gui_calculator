from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from game import Player, desc
from qtcal import CalPyQt


class EclipsePyQt(Player, QMainWindow):
    def __init__(self):
        QWidget.__init__(self)

        self.next = None
        self.setGeometry(100, 100, 1400, 600)
        self.setFixedSize(1000, 500)
        self.setWindowTitle("Eclipse PyQt")
        self.setStyleSheet("background-color: #FAFAFF")
        self.createMenu()
        self.introMenu()

        self.show()

    def introMenu(self):
        self.pnumber = QComboBox(self)
        self.pnumber.addItems(["2", "3", "4"])
        self.pnumber.setGeometry(750, 200, 200, 50)
        self.pnumber.setStyleSheet("font-size: 15px")
        self.pnumber.currentIndexChanged.connect(self.pNumberChange)
        self.p1 = QLineEdit(self)
        self.p1.setGeometry(350, 200, 150, 32)
        self.p1.setStyleSheet("font-size: 15px")
        self.p1.setMaxLength(15)
        self.p2 = QLineEdit(self)
        self.p2.setGeometry(350, 250, 150, 32)
        self.p2.setMaxLength(15)
        self.p3 = QLineEdit(self)
        self.p3.setGeometry(350, 300, 150, 32)
        self.p3.setMaxLength(15)
        self.p4 = QLineEdit(self)
        self.p4.setGeometry(350, 350, 150, 32)
        self.p4.setMaxLength(15)
        self.p3.setDisabled(True)
        self.p4.setDisabled(True)
        self.next = QPushButton("Dalej", self)
        self.next.setGeometry(750, 300, 200, 50)
        self.next.clicked.connect(self.goNext)
        self.labelt = QLabel("Eclipse Kalkulator", self)
        self.labelt.setGeometry(350, 10, 600, 100)
        self.labelt.setStyleSheet("font-size: 50px")
        self.labeln = QLabel("Nazwy graczy", self)
        self.labeln.setGeometry(200, 100, 200, 50)
        self.labeln.setStyleSheet("font-size: 20px")
        self.labell = QLabel("Liczba graczy", self)
        self.labell.setGeometry(750, 100, 200, 50)
        self.labell.setStyleSheet("font-size: 20px")
        self.pn1 = QLabel("Nazwa gracza nr 1.", self)
        self.pn1.setGeometry(200, 200, 150, 32)
        self.pn1.setStyleSheet("font-size: 15px")
        self.pn2 = QLabel("Nazwa gracza nr 2.", self)
        self.pn2.setGeometry(200, 250, 150, 32)
        self.pn2.setStyleSheet("font-size: 15px")
        self.pn2 = QLabel("Nazwa gracza nr 3.", self)
        self.pn2.setGeometry(200, 300, 150, 32)
        self.pn2.setStyleSheet("font-size: 15px")
        self.pn2 = QLabel("Nazwa gracza nr 4.", self)
        self.pn2.setGeometry(200, 350, 150, 32)
        self.pn2.setStyleSheet("font-size: 15px")


    def pNumberChange(self, i):
        if int(self.pnumber.itemText(i)) < 3:
            self.p3.setDisabled(True)
            self.p3.clear()
        else:
            self.p3.setDisabled(False)
        if int(self.pnumber.itemText(i)) < 4:
            self.p4.setDisabled(True)
            self.p4.clear()
        else:
            self.p4.setDisabled(False)

    def goNext(self):
        Players = list()
        p1 = Player()
        p1.Name = self.p1.text()
        if p1.Name == "":
            p1.Name = "Gracz niebieski"
        p1.Color = "blue"
        Players.append(p1)
        p2 = Player()
        p2.Name = self.p2.text()
        if p2.Name == "":
            p2.Name = "Gracz czerwony"
        p2.Color = "red"
        Players.append(p2)
        if int(self.pnumber.currentText()) >= 3:
            p3 = Player()
            p3.Name = self.p3.text()
            if p3.Name == "":
                p3.Name = "Gracz fioletowy"
            p3.Color = "purple"
            Players.append(p3)
        if int(self.pnumber.currentText()) >= 4:
            p4 = Player()
            p4.Name = self.p4.text()
            if p4.Name == "":
                p4.Name = "Gracz zielony"
            p4.Color = "green"
            Players.append(p4)
        self.close()
        self.next = CalPyQt(Players)

    def createMenu(self):
        menuBar = QMenuBar(self)
        info = QMenu("&Info", self)
        menuBar.setStyleSheet("color: black")
        info.setStyleSheet("color: black")
        menuBar.addMenu(info)
        action = QAction("&Opis aplikacji", self)
        info.addAction(action)
        action.triggered.connect(self.showInfo)
        self.setMenuBar(menuBar)

    def showInfo(self):
        self.infoWidget = QWidget()
        self.infoWidget.setGeometry(100, 105, 400, 100)
        self.infoWidget.setFixedSize(300, 100)
        self.infoWidget.setStyleSheet("color: black;background-color: white")
        self.infoWidget.setWindowTitle("Opis aplikacji")
        infoText = QLabel(desc.Opis ,self.infoWidget)
        infoText.move(20, 20)
        infoText.setWordWrap(True)

        self.infoWidget.show()
