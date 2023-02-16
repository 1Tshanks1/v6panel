from PySide6.QtWidgets import QApplication, QStackedWidget, QWidget, QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide6.QtGui import QIcon, QPixmap, QColor, QFont, QPalette
from PySide6.QtCore import QCoreApplication,QTimer
from thirdpage import Ui_thirdPage
from backend import device
from serial.tools import list_ports
import sys
import numpy as np
from digi.xbee.devices import XBeeDevice
import pyqtgraph as pg

x = []
i=0
y = []

xbee = XBeeDevice("COM4",57600)
xbee.open()

class secondPage(QWidget, Ui_thirdPage):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

        self.timer=QTimer()
        self.timer.setInterval(195)
        self.timer.timeout.connect(self.draw)
        self.nextButton.clicked.connect(self.start)
        

    def start(self):
        self.timer.start()

    
    def draw(self):
        global x
        pen = pg.mkPen(color=(255, 0, 0),width=1)
        comingdata = xbee.read_data()
        if comingdata != None:
            seperatedData = comingdata.data.decode(
                    'utf8', 'strict').split(",")
            y.append(float(seperatedData[0]))
            x.append(float(seperatedData[1]))

        
        self.device1AT.setLabel('left', 'Altitude ', color='red', size=30)
        self.device1AT.setLabel('bottom', 'Time', color='red', size=30)

        self.device1AT.plot(x, y,name="Data 1" ,pen=pen)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = secondPage()
    

    window.showMaximized()

    app.exec()