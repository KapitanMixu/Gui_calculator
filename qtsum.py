from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from game import Player, Board, pointsCal, desc


class SumPyQt(Player, QMainWindow):
    def __init__(self, data):
        QWidget.__init__(self)

        self.S = data
        self.SLen = len(data)
        self.PNum = 0
        self.setGeometry(100, 100, 1000, 500)
        self.setFixedSize(1000, 500)
        self.setWindowTitle("Eclipse PyQt")
        self.setStyleSheet("background-color: #FAFAFF")
        self.createMenu()
        self.sumMenu(self.S)

        self.show()

    def sumMenu(self, Score):
        self.label0 = QLabel("Wyniki", self)
        self.label0.setGeometry(450, 20, 600, 100)
        self.label0.setStyleSheet("font-size: 50px")
        self.g1 = QLabel("1. miejsce", self)
        self.g1.setGeometry(150, 120, 200, 100)
        self.g1.setStyleSheet("font-size: 30px")
        self.g2 = QLabel("2. miejsce", self)
        self.g2.setGeometry(150, 190, 200, 100)
        self.g2.setStyleSheet("font-size: 30px")
        self.g3 = QLabel("", self)
        self.g3.setGeometry(150, 260, 200, 100)
        self.g3.setStyleSheet("font-size: 30px")
        self.g4 = QLabel("", self)
        self.g4.setGeometry(150, 330, 200, 100)
        self.g4.setStyleSheet("font-size: 30px")
        self.player1 = QLabel("", self)
        self.player1.setGeometry(350, 120, 300, 100)
        self.player2 = QLabel("", self)
        self.player2.setGeometry(350, 190, 300, 100)
        self.player3 = QLabel("", self)
        self.player3.setGeometry(350, 260, 300, 100)
        self.player4 = QLabel("", self)
        self.player4.setGeometry(350, 330, 300, 100)
        self.pkt1 = QLabel("", self)
        self.pkt1.setGeometry(650, 120, 300, 100)
        self.pkt1.setStyleSheet("font-size: 30px")
        self.pkt2 = QLabel("", self)
        self.pkt2.setGeometry(650, 190, 300, 100)
        self.pkt2.setStyleSheet("font-size: 30px")
        self.pkt3 = QLabel("", self)
        self.pkt3.setGeometry(650, 260, 300, 100)
        self.pkt3.setStyleSheet("font-size: 30px")
        self.pkt4 = QLabel("", self)
        self.pkt4.setGeometry(650, 330, 300, 100)
        self.pkt4.setStyleSheet("font-size: 30px")

        self.getScore(Score)

    def getScore(self, S):
        S.sort(key=lambda x: x.points, reverse=True)
        self.player1.setText(S[0].Name)
        self.pkt1.setText("{} pkt.".format(S[0].points))
        self.player1.setStyleSheet("font-size: 30px; color: {}".format(S[0].Color))
        self.player2.setText(S[1].Name)
        self.player2.setStyleSheet("font-size: 30px; color: {}".format(S[1].Color))
        self.pkt2.setText("{} pkt.".format(S[1].points))
        if len(S) >= 3:
            self.g3.setText("3. miejsce")
            self.player3.setText(S[2].Name)
            self.player3.setStyleSheet("font-size: 30px; color: {}".format(S[2].Color))
            self.pkt3.setText("{} pkt.".format(S[2].points))
        if len(S) == 4:
            self.g4.setText("4. miejsce")
            self.player4.setText(S[3].Name)
            self.player4.setStyleSheet("font-size: 30px; color: {}".format(S[3].Color))
            self.pkt4.setText("{} pkt.".format(S[3].points))

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