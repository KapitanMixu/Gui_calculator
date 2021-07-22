import gi
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
gi.require_version('Gtk', '3.0')
from gi.overrides import Gtk


class Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eclipse")
        self.setLayout(QVBoxLayout())
        # setting geometry
        self.setGeometry(100, 100, 1400, 600)
        # calling method
        self.startComponents()
        # showing all the widgets
        self.show()

    def startComponents(self):



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # setting title
        self.setWindowTitle("Eclipse")
        self.setLayout(QVBoxLayout())
        # setting geometry
        self.setGeometry(100, 100, 1400, 600)
        # calling method
        self.UiComponents()
        # showing all the widgets
        self.show()
        #self.setStyleSheet("QMainWindow{"
        #                   "background-image: url(galaxy.jpg);"
        #                   "}")

    # method for widgets

    def UiComponents(self):
        center = QPushButton("Test", self)
        center.setGeometry(200, 200, 90, 90)
        center.clicked.connect(self.clickme)
        center.setStyleSheet("""color: #333;
        border: 2px solid #555;
        border-radius: 20px;
        border-style: outset;
        background: qradialgradient(
            cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
        radius: 1.35, stop: 0 #fff, stop: 1 #888
        );
        padding: 5px;""")
        self.w1 = QPushButton("Red", self)
        self.w1.setGeometry(150, 150, 50, 50)
        self.w1.setCheckable(True)
        self.w1.clicked[bool].connect(self.changeColor)
        self.w1.setStyleSheet("background-color: blue")

        self.w2 = QPushButton("Green", self)
        self.w2.setGeometry(290, 290, 50, 50)
        self.w2.setCheckable(True)
        self.w2.clicked[bool].connect(self.changeColor)
        self.w2.setStyleSheet("background-color: blue")

    # action method

    def clickme(self):
        # printing pressed
        print("pressed")

    def changeColor(self, down):
        source = self.sender()
        # if button is checked
        if down:
            source.setStyleSheet("background-color: red")
        # if it is unchecked
        else:
            source.setStyleSheet("background-color: green")

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())