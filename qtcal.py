from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from game import Player, Board, pointsCal, desc
from qtsum import SumPyQt


class CalPyQt(Player, Board, QMainWindow):
    def __init__(self, data):
        QWidget.__init__(self)

        self.sum = None

        self.P = data
        self.PLen = len(data)
        self.PNum = 0
        self.setGeometry(100, 100, 1000, 600)
        self.setFixedSize(1000, 500)
        self.setWindowTitle("Eclipse PyQt")
        self.setStyleSheet("background-color: #FAFAFF")

        self.createMenu()
        self.calMenu(self.P[0])

        self.show()

    def calMenu(self, PNow):
        self.PlayerNow = PNow
        self.BoardNow = Board()
        self.PlayerName = QLabel(self)
        self.PlayerName.setText(self.PlayerNow.Name)
        self.label0 = QLabel("Gracz", self)
        self.label0.setGeometry(730, 300, 200, 50)
        self.label0.setStyleSheet("font-size: 20px")
        self.PlayerName.setGeometry(730, 350, 200, 50)
        self.PlayerName.setStyleSheet("color: {}; border-radius: 20px; font-size: 20px;".format(self.PlayerNow.Color))
        self.next = QPushButton("Dalej", self)
        self.next.setGeometry(730, 400, 200, 50)
        self.next.clicked.connect(self.goNex)

        #Mapa galaktyki
        self.label1 = QLabel("Mapa galaktyki", self)
        self.label1.setGeometry(40, 10, 200, 50)
        self.label1.setStyleSheet("font-size: 20px")
        self.center = QPushButton("Centrum", self)
        self.center.setGeometry(170, 170, 90, 90)
        self.center.setCheckable(True)
        self.center.clicked[bool].connect(self.changeColor)
        self.center.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")

        #SEKCJA WEWNĘTRZNA
        self.w1 = QPushButton("W1", self)
        self.w1.setGeometry(190, 110, 50, 50)
        self.w1.setCheckable(True)
        self.w1.clicked[bool].connect(self.changeColor)
        self.w1.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.w2 = QPushButton("W2", self)
        self.w2.setGeometry(270, 150, 50, 50)
        self.w2.setCheckable(True)
        self.w2.clicked[bool].connect(self.changeColor)
        self.w2.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.w3 = QPushButton("W3", self)
        self.w3.setGeometry(270, 230, 50, 50)
        self.w3.setCheckable(True)
        self.w3.clicked[bool].connect(self.changeColor)
        self.w3.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.w4 = QPushButton("W4", self)
        self.w4.setGeometry(190, 270, 50, 50)
        self.w4.setCheckable(True)
        self.w4.clicked[bool].connect(self.changeColor)
        self.w4.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.w5 = QPushButton("W5", self)
        self.w5.setGeometry(110, 150, 50, 50)
        self.w5.setCheckable(True)
        self.w5.clicked[bool].connect(self.changeColor)
        self.w5.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.w6 = QPushButton("W6", self)
        self.w6.setGeometry(110, 230, 50, 50)
        self.w6.setCheckable(True)
        self.w6.clicked[bool].connect(self.changeColor)
        self.w6.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")

        #SEKCJA ZEWNĘTRZNA
        self.z1 = QPushButton("Z1", self)
        self.z1.setGeometry(195, 65, 40, 40)
        self.z1.setCheckable(True)
        self.z1.clicked[bool].connect(self.changeColor)
        self.z1.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.z2 = QPushButton("Z2", self)
        self.z2.setGeometry(270, 90, 40, 40)
        self.z2.setCheckable(True)
        self.z2.clicked[bool].connect(self.changeColor)
        self.z2.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.z3 = QPushButton("Z3", self)
        self.z3.setGeometry(330, 140, 40, 40)
        self.z3.setCheckable(True)
        self.z3.clicked[bool].connect(self.changeColor)
        self.z3.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.z4 = QPushButton("Z4", self)
        self.z4.setGeometry(345, 195, 40, 40)
        self.z4.setCheckable(True)
        self.z4.clicked[bool].connect(self.changeColor)
        self.z4.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.z5 = QPushButton("Z5", self)
        self.z5.setGeometry(330, 250, 40, 40)
        self.z5.setCheckable(True)
        self.z5.clicked[bool].connect(self.changeColor)
        self.z5.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.z6 = QPushButton("Z6", self)
        self.z6.setGeometry(270, 300, 40, 40)
        self.z6.setCheckable(True)
        self.z6.clicked[bool].connect(self.changeColor)
        self.z6.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.z7 = QPushButton("Z7", self)
        self.z7.setGeometry(195, 325, 40, 40)
        self.z7.setCheckable(True)
        self.z7.clicked[bool].connect(self.changeColor)
        self.z7.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.z8 = QPushButton("Z8", self)
        self.z8.setGeometry(120, 300, 40, 40)
        self.z8.setCheckable(True)
        self.z8.clicked[bool].connect(self.changeColor)
        self.z8.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.z9 = QPushButton("Z9", self)
        self.z9.setGeometry(60, 250, 40, 40)
        self.z9.setCheckable(True)
        self.z9.clicked[bool].connect(self.changeColor)
        self.z9.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.z10 = QPushButton("Z10", self)
        self.z10.setGeometry(45, 195, 40, 40)
        self.z10.setCheckable(True)
        self.z10.clicked[bool].connect(self.changeColor)
        self.z10.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.z11 = QPushButton("Z11", self)
        self.z11.setGeometry(60, 140, 40, 40)
        self.z11.setCheckable(True)
        self.z11.clicked[bool].connect(self.changeColor)
        self.z11.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
        self.z12 = QPushButton("Z12", self)
        self.z12.setGeometry(120, 90, 40, 40)
        self.z12.setCheckable(True)
        self.z12.clicked[bool].connect(self.changeColor)
        self.z12.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")

        #Obrzeża
        self.label2 = QLabel("Obrzeża", self)
        self.label2.setGeometry(40, 360, 100, 30)
        self.label2.setStyleSheet("font-size: 20px")
        self.os = QSlider(Qt.Horizontal, self)
        self.os.setRange(0, 20)
        self.os.setFocusPolicy(Qt.NoFocus)
        self.os.setPageStep(1)
        self.os.setGeometry(80, 420, 180, 20)
        self.os.valueChanged.connect(self.oChange)
        self.ol = QLabel('0', self)
        self.ol.move(275, 415)

        #Technologie
        self.label3 = QLabel("Technologie", self)
        self.label3.setGeometry(450, 10, 150, 30)
        self.label3.setStyleSheet("font-size: 20px")
        self.label31 = QLabel("Technologie wojskowe", self)
        self.label31.setGeometry(450, 50, 150, 20)
        self.label31.setStyleSheet("font-size: 15px")
        self.label32 = QLabel("Technologie naukowe", self)
        self.label32.setGeometry(450, 110, 150, 30)
        self.label32.setStyleSheet("font-size: 15px")
        self.label33 = QLabel("Technologie cywilne", self)
        self.label33.setGeometry(450, 170, 150, 30)
        self.label33.setStyleSheet("font-size: 15px")

        self.t1s = QSlider(Qt.Horizontal, self)
        self.t1s.setRange(0, 7)
        self.t1s.setFocusPolicy(Qt.NoFocus)
        self.t1s.setPageStep(1)
        self.t1s.setGeometry(450, 80, 180, 20)
        self.t1s.valueChanged.connect(self.t1Change)
        self.t1l = QLabel('0', self)
        self.t1l.move(635, 75)
        self.t2s = QSlider(Qt.Horizontal, self)
        self.t2s.setRange(0, 7)
        self.t2s.setFocusPolicy(Qt.NoFocus)
        self.t2s.setPageStep(1)
        self.t2s.setGeometry(450, 140, 180, 20)
        self.t2s.valueChanged.connect(self.t2Change)
        self.t2l = QLabel('0', self)
        self.t2l.move(635, 135)
        self.t3s = QSlider(Qt.Horizontal, self)
        self.t3s.setRange(0, 7)
        self.t3s.setFocusPolicy(Qt.NoFocus)
        self.t3s.setPageStep(1)
        self.t3s.setGeometry(450, 200, 180, 20)
        self.t3s.valueChanged.connect(self.t3Change)
        self.t3l = QLabel('0', self)
        self.t3l.move(635, 195)

        #Dodatkowe technologie
        self.label4 = QLabel("Technologie dodatkowe", self)
        self.label4.setGeometry(450, 260, 250, 30)
        self.label4.setStyleSheet("font-size: 20px")
        self.st1 = QCheckBox("Dodatkowe fundusze na edukację", self)
        self.st1.setChecked(False)
        self.st1.setGeometry(450, 300, 250, 20)
        self.st1.setStyleSheet("font-size: 15px;")
        self.st2 = QCheckBox("Krąg centralny", self)
        self.st2.setChecked(False)
        self.st2.setGeometry(450, 330, 200, 20)
        self.st2.setStyleSheet("font-size: 15px;")
        self.st3 = QCheckBox("Rządy na odległość", self)
        self.st3.setChecked(False)
        self.st3.setGeometry(450, 360, 200, 20)
        self.st3.setStyleSheet("font-size: 15px;")
        self.st4 = QCheckBox("Telewizja wojskowa", self)
        self.st4.setChecked(False)
        self.st4.setGeometry(450, 390, 200, 20)
        self.st4.setStyleSheet("font-size: 15px;")

        #EMBLEMATY
        self.label5 = QLabel("Emblematy", self)
        self.label5.setGeometry(730, 10, 250, 30)
        self.label5.setStyleSheet("font-size: 20px")
        self.e1 = QComboBox(self)
        self.e1.addItems(["0", "1", "2", "3", "4"])
        self.e1.move(830, 50)
        self.le1 = QLabel('Emblemat 1', self)
        self.le1.move(730, 50)
        self.le1.setStyleSheet("font-size: 15px")
        self.e2 = QComboBox(self)
        self.e2.addItems(["0", "1", "2", "3", "4"])
        self.e2.move(830, 110)
        self.le2 = QLabel('Emblemat 2', self)
        self.le2.move(730, 110)
        self.le2.setStyleSheet("font-size: 15px")
        self.e3 = QComboBox(self)
        self.e3.addItems(["0", "1", "2", "3", "4"])
        self.e3.move(830, 170)
        self.le3 = QLabel('Emblemat 3', self)
        self.le3.move(730, 170)
        self.le3.setStyleSheet("font-size: 15px")
        self.e4 = QComboBox(self)
        self.e4.addItems(["0", "1", "2", "3", "4"])
        self.e4.move(830, 230)
        self.le4 = QLabel('Emblemat 4', self)
        self.le4.move(730, 230)
        self.le4.setStyleSheet("font-size: 15px")

    def t1Change(self, value):
        self.t1l.setText(str(value))

    def t2Change(self, value):
        self.t2l.setText(str(value))

    def t3Change(self, value):
        self.t3l.setText(str(value))

    def oChange(self, value):
        self.ol.setText(str(value))

    def goNex(self):
        if self.PNum == 0:
            self.Score = list()
        self.PNum += 1
        if self.PNum < self.PLen:
            self.savePlayer(self.Score)
            self.PlayerNow = self.P[self.PNum]
            self.PlayerName.setText(self.PlayerNow.Name)
            self.PlayerName.setStyleSheet("color: {}; border-radius: 20px;  font-size: 20px;".format(self.PlayerNow.Color))
            self.resetMap()
        else:
            self.savePlayer(self.Score)
            self.close()
            self.sum = SumPyQt(self.Score)

    def savePlayer(self, Score):
        #Obrzeża
        self.PlayerNow.Hexs[3] = self.os.value()
        self.os.setRange(0, self.os.maximum() - self.os.value())
        self.os.setValue(0)

        #Technologie
        self.PlayerNow.Techs[0] = self.t1s.value()
        self.t1s.setValue(0)
        self.PlayerNow.Techs[1] = self.t2s.value()
        self.t2s.setValue(0)
        self.PlayerNow.Techs[2] = self.t3s.value()
        self.t3s.setValue(0)

        #Technologie specjalne
        if self.st1.isChecked():
            self.PlayerNow.Stechs[0] = 1
            self.st1.setChecked(False)
        if self.st2.isChecked():
            self.PlayerNow.Stechs[1] = 1
            self.st2.setChecked(False)
        if self.st3.isChecked():
            self.PlayerNow.Stechs[2] = 1
            self.st3.setChecked(False)
        if self.st4.isChecked():
            self.PlayerNow.Stechs[3] = 1
            self.st4.setChecked(False)

        #Emblematy
        self.PlayerNow.Emb[0] = int(self.e1.currentText())
        self.e1.setCurrentIndex(0)
        self.PlayerNow.Emb[1] = int(self.e2.currentText())
        self.e2.setCurrentIndex(0)
        self.PlayerNow.Emb[2] = int(self.e3.currentText())
        self.e3.setCurrentIndex(0)
        self.PlayerNow.Emb[3] = int(self.e4.currentText())
        self.e4.setCurrentIndex(0)

        #liczenie punktów
        self.PlayerNow.points = pointsCal(self.PlayerNow)
        Score.append(self.PlayerNow)


    def resetMap(self):
        ###MAP
        #SEKJA ZEWNĘTRZNA
        if self.BoardNow.z[0] == 1:
            self.z1.setEnabled(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[0] = 0
        if self.BoardNow.z[1] == 1:
            self.z2.setEnabled(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[1] = 0
        if self.BoardNow.z[2] == 1:
            self.z3.setEnabled(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[2] = 0
        if self.BoardNow.z[3] == 1:
            self.z4.setEnabled(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[3] = 0
        if self.BoardNow.z[4] == 1:
            self.z5.setEnabled(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[4] = 0
        if self.BoardNow.z[5] == 1:
            self.z6.setEnabled(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[5] = 0
        if self.BoardNow.z[6] == 1:
            self.z7.setEnabled(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[6] = 0
        if self.BoardNow.z[7] == 1:
            self.z8.setEnabled(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[7] = 0
        if self.BoardNow.z[8] == 1:
            self.z9.setEnabled(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[8] = 0
        if self.BoardNow.z[9] == 1:
            self.z10.setEnabled(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[9] = 0
        if self.BoardNow.z[10] == 1:
            self.z11.setEnabled(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[10] = 0
        if self.BoardNow.z[11] == 1:
            self.z12.setEnabled(False)
            self.PlayerNow.Hexs[2] -= 1
            self.BoardNow.z[11] = 0
        #SEKCJA WEWNĘTRZNA
        if self.BoardNow.w[0] == 1:
            self.w1.setEnabled(False)
            self.PlayerNow.Hexs[1] -= 1
            self.BoardNow.w[0] = 0
        if self.BoardNow.w[1] == 1:
            self.w2.setEnabled(False)
            self.PlayerNow.Hexs[1] -= 1
            self.BoardNow.w[1] = 0
        if self.BoardNow.w[2] == 1:
            self.w3.setEnabled(False)
            self.PlayerNow.Hexs[1] -= 1
            self.BoardNow.w[2] = 0
        if self.BoardNow.w[3] == 1:
            self.w4.setEnabled(False)
            self.PlayerNow.Hexs[1] -= 1
            self.BoardNow.w[3] = 0
        if self.BoardNow.w[4] == 1:
            self.w5.setEnabled(False)
            self.PlayerNow.Hexs[1] -= 1
            self.BoardNow.w[4] = 0
        if self.BoardNow.w[5] == 1:
            self.w6.setEnabled(False)
            self.PlayerNow.Hexs[1] -= 1
            self.BoardNow.w[5] = 0
        #Centrum
        if self.BoardNow.c == 1:
            self.center.setEnabled(False)
            self.PlayerNow.Hexs[0] = 0
            self.BoardNow.c = 0

    def changeColor(self, down):
        source = self.sender()
        if down:
            source.setStyleSheet("background-color: {}; border-radius: 20px;".format(self.PlayerNow.Color))
            if source.text()[0] == "Z":
                for x in range(12):
                    if source.text()[1:] == str(x + 1):
                        self.BoardNow.z[x] = 1
                        self.PlayerNow.Hexs[2] += 1
            elif source.text()[0] == "W":
                for x in range(6):
                    if source.text()[1:] == str(x + 1):
                        self.BoardNow.w[x] = 1
                        self.PlayerNow.Hexs[1] += 1
            else:
                self.BoardNow.c = 1
                self.PlayerNow.Hexs[0] = 1
        else:
            source.setStyleSheet("background-color: #c7c9c8; border-radius: 20px;")
            if source.text()[0] == "Z":
                for x in range(12):
                    if source.text()[1:] == str(x + 1):
                        self.BoardNow.z[x] = 0
                        self.PlayerNow.Hexs[2] -= 1
            elif source.text()[0] == "W":
                for x in range(6):
                    if source.text()[1:] == str(x + 1):
                        self.BoardNow.w[x] = 0
                        self.PlayerNow.Hexs[1] -= 1
            else:
                self.BoardNow.c = 0
                self.PlayerNow.Hexs[0] = 0

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