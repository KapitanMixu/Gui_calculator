import gi
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
gi.require_version('Gtk', '3.0')
from gi.overrides import Gtk
from qteclipse import EclipsePyQt
from gtkeclipse import EclipseGtk


class Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.recorder = None

        self.setStyleSheet("background-color: #FFFFFF")

        self.setGeometry(800, 300, 200, 200)
        self.setWindowTitle("Wybierz GUI")

        pyqtButton = QPushButton("GUI PyQt", self)
        pyqtButton.setGeometry(40, 40, 120, 40)
        pyqtButton.clicked.connect(self.pyqtBtnClicked)

        gtkButton = QPushButton("GUI GTK", self)
        gtkButton.setGeometry(40, 100, 120, 40)
        gtkButton.clicked.connect(self.gtkBtnClicked)

        self.show()

    def pyqtBtnClicked(self):
        self.close()
        self.recorder = EclipsePyQt()

    def gtkBtnClicked(self):
        self.close()
        self.recorder = EclipseGtk()

# create pyqt5 app


if __name__ == '__main__':

    app = QApplication(sys.argv)

    mainWindow = Start()

    sys.exit(app.exec_())

