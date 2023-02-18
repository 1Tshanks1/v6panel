from PySide6.QtWidgets import QApplication, QStackedWidget, QWidget, QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide6.QtGui import QIcon, QPixmap, QColor, QFont, QPalette
from PySide6.QtCore import QCoreApplication,QTimer
import pyqtgraph as pg
from firstpage import Ui_pageOne
from secondpage import  Ui_secondthPage
from thirdpage import Ui_thirdPage
from backend import device
from serial.tools import list_ports
import sys


xbeeDevice1 = None
xbeeDevice2 = None
xbeeDevice3 = None
count = 0
remotecount = 0
time = []
i=0
class firstPage(QWidget, Ui_pageOne):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.scanComs()
        self.reloadButton.clicked.connect(self.scanComs)
        self.nextButton.clicked.connect(self.nextPage)
        self.addButton.clicked.connect(self.add)
        self.remoteDeviceAddButton.clicked.connect(self.addRemoteDevice)

    def scanComs(self):
        self.portBox.clear()
        self.ports = list_ports.comports()
        for port in self.ports:
            self.portBox.addItem(port.device)

    def nextPage(self):
        if count == 0:
            errormsg = QMessageBox()
            errormsg.setText("Please add at least 1 device!")
            errormsg.setWindowTitle("Error")
            errormsg.exec()
        elif count == 1:
            
            
            window.setCurrentIndex(window.currentIndex() + 1)

            secondPage.getData(second)
            secondPage.getData2(second)
            

    def add(self):
        global xbeeDevice1, xbeeDevice2, xbeeDevice3, count, remotecount, deviceNames, errormsg, succesmsg
        deviceNames = []
        succesmsg = QMessageBox()
        succesmsg.setWindowTitle("Succesful")
        succesmsg.setText("You have succesfully connected a device.")
        errormsgsec = QMessageBox()
        errormsgsec.setWindowTitle("Error")
        errormsgsec.setText(
            "Flight name and Device name have to be longer than 1 character!!")
        if count == 0 and len(self.flightName.text()) > 0 and len(self.deviceName.text()) > 0 and self.deviceName.text().lower() not in deviceNames:

            xbeeDevice1 = device(self.flightName.text(), self.deviceName.text(
            ), self.portBox.currentText(), self.baudBox.currentText())
            deviceNames.append(self.deviceName.text().lower())

            count += 1
            self.localBox.addItem(self.deviceName.text())
            succesmsg.exec()

        elif len(self.flightName.text()) == 0 or len(self.deviceName.text()) == 0:
            errormsgsec.exec()

        else:
            errormsg = QMessageBox()
            errormsg.setWindowTitle("Error")
            errormsg.setText(
                "You have reached maximum number of devices!!\nYou cannot add a new device.")
            errormsg.exec()

    def addRemoteDevice(self):
        global remotecount, deviceNames, errormsg, succesmsg
        errormsgsec = QMessageBox()
        errormsgsec.setWindowTitle("Error")
        errormsgsec.setText(
            "Remote Device name have to be longer than 1 character!!")
        if remotecount <= 2 and len(self.remoteDeviceName.text()) > 1:

            xbeeDevice1.createRemoteDevice(self.remoteDeviceAdress.text())
            remotecount += 1
            if remotecount == 1:
                xbeeDevice1.remoteDevice1.name = self.remoteDeviceName.text()
                succesmsg.exec()
            elif remotecount == 2:
                xbeeDevice1.remoteDevice2.name = self.remoteDeviceName.text()
                succesmsg.exec()

        elif len(self.remoteDeviceName.text()) == 0:
            errormsgsec.exec()

        else:
            errormsg.exec()


class secondPage(QWidget, Ui_secondthPage):
    global remotecount
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.nextButton.clicked.connect(self.nextPage)
        self.backButton.clicked.connect(self.previousPage)
        self.resButton.clicked.connect(self.getData)
        self.setButton.clicked.connect(self.setData)
        self.resButton_2.clicked.connect(self.getData2)
        self.setButton_2.clicked.connect(self.setData2)
        
            
        

    def setData(self):

        xbeeDevice1.remoteDevice1.initialLatitude = xbeeDevice1.remoteDevice1.latitude[-1]
        xbeeDevice1.remoteDevice1.initialLongtitude = xbeeDevice1.remoteDevice1.longtitude[-1]
        xbeeDevice1.remoteDevice1.initialAltitude = xbeeDevice1.remoteDevice1.altitude[-1]
        xbeeDevice1.remoteDevice1.initialVelocity = xbeeDevice1.remoteDevice1.velocity[-1]

    def setData2(self):

        
        xbeeDevice1.remoteDevice2.initialLatitude = xbeeDevice1.remoteDevice2.latitude[-1]
        xbeeDevice1.remoteDevice2.initialLongtitude = xbeeDevice1.remoteDevice2.longtitude[-1]
        xbeeDevice1.remoteDevice2.initialAltitude = xbeeDevice1.remoteDevice2.altitude[-1]
        xbeeDevice1.remoteDevice2.initialVelocity = xbeeDevice1.remoteDevice2.velocity[-1]

    def getData(self):

        self.devicename1.setText(xbeeDevice1.remoteDevice1.name)
        xbeeDevice1.readData(xbeeDevice1.remoteDevice1)
        if xbeeDevice1.remoteDevice1.altitude and xbeeDevice1.remoteDevice1.longtitude and xbeeDevice1.remoteDevice1.latitude and xbeeDevice1.remoteDevice1.velocity:
            self.altitudeLabel.setText(str(xbeeDevice1.remoteDevice1.altitude[-1]))
            self.longtitudeLabel.setText(
                str(xbeeDevice1.remoteDevice1.longtitude[-1]))
            self.velocityLabel.setText(str(xbeeDevice1.remoteDevice1.velocity[-1]))
            self.latitudeLabel.setText(str(xbeeDevice1.remoteDevice1.latitude[-1]))

    def getData2(self):

        self.devicename1.setText(xbeeDevice1.remoteDevice2.name)
        self.devicename2.setText(xbeeDevice1.remoteDevice2.name)
        xbeeDevice1.readData(xbeeDevice1.remoteDevice2)
        self.altitudeLabel_2.setText(
            xbeeDevice1.remoteDevice2.altitude[-1])
        self.longtitudeLabel_2.setText(
            xbeeDevice1.remoteDevice2.longtitude[-1])
        self.velocityLabel_2.setText(
            xbeeDevice1.remoteDevice2.velocity[-1])
        self.latitudeLabel_2.setText(
            xbeeDevice1.remoteDevice2.latitude[-1])

    def nextPage(self):
        window.setCurrentIndex(window.currentIndex() + 1)

    def previousPage(self):
        window.setCurrentIndex(window.currentIndex() - 1)

class thirdPage(QWidget, Ui_thirdPage):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

        self.timer=QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.draw)
        self.startButton.clicked.connect(self.start)
        self.nextButton.clicked.connect(self.nextPage)
        self.backButton.clicked.connect(self.previousPage)

        

    def start(self):
        self.timer.start()
        xbeeDevice1.clear()

    
    def draw(self):
        global time,i
        pen = pg.mkPen(color=(255, 0, 0),width=1)
        
        xbeeDevice1.readData(xbeeDevice1.remoteDevice1)
        if remotecount == 2:
        
            xbeeDevice1.readData(xbeeDevice1.remoteDevice2)
        i+=1
        time.append(i)
        
        self.remoteDeviceName.setText(xbeeDevice1.remoteDevice1.name)
        self.remoteDeviceAltitude.setText(str(xbeeDevice1.remoteDevice1.altitude[-1]))
        self.remoteDeviceLongtitude.setText(str(xbeeDevice1.remoteDevice1.longtitude[-1]))
        self.remoteDeviceVelocity.setText(str(xbeeDevice1.remoteDevice1.velocity[-1]))
        self.remoteDeviceLatitude.setText(str(xbeeDevice1.remoteDevice1.latitude[-1]))
        if remotecount == 2:
        
            self.remoteDeviceName2_2.setText(xbeeDevice1.remoteDevice2.name)
            self.remoteDevice2Altitude.setText(str(xbeeDevice1.remoteDevice2.altitude[-1]))
            self.remoteDevice2Longtitude.setText(str(xbeeDevice1.remoteDevice2.longtitude[-1]))
            self.remoteDevice2Velocity.setText(str(xbeeDevice1.remoteDevice2.velocity[-1]))
            self.remoteDevice2Latitude.setText(str(xbeeDevice1.remoteDevice2.latitude[-1]))
        else:
            self.remoteDeviceName2_2.setText("NONE")
            self.remoteDevice2Altitude.setText("NONE")
            self.remoteDevice2Longtitude.setText("NONE")
            self.remoteDevice2Velocity.setText("NONE")
            self.remoteDevice2Latitude.setText("NONE")
        
        
        self.device1AT.setLabel('left', 'Altitude ', color='white', size=30)
        self.device1AT.setLabel('bottom', 'Time', color='white', size=30)

        self.device2AT.setLabel('left', 'Altitude ', color='white', size=30)
        self.device2AT.setLabel('bottom', 'Time', color='white', size=30)

        self.device2VT.setLabel('left', 'Velocity ', color='white', size=30)
        self.device2VT.setLabel('bottom', 'Time', color='white', size=30)

        self.device1VT.setLabel('left', 'Velocity ', color='white', size=30)
        self.device1VT.setLabel('bottom', 'Time', color='white', size=30)

        self.device1AT.plot(time, xbeeDevice1.remoteDevice1.altitude,name="Data 1" ,pen=pen)
        self.device1VT.plot(time, xbeeDevice1.remoteDevice1.velocity,name="Data 1" ,pen=pen)
        self.device2VT.plot(time, xbeeDevice1.remoteDevice2.velocity,name="Data 1" ,pen=pen)
        self.device2AT.plot(time, xbeeDevice1.remoteDevice2.altitude,name="Data 1" ,pen=pen)

    def nextPage(self):
        window.setCurrentIndex(window.currentIndex() + 1)

    def previousPage(self):
        window.setCurrentIndex(window.currentIndex() - 1)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = QStackedWidget()
    first = firstPage()
    second = secondPage()
    third = thirdPage()
    

    window.setWindowTitle("Versiyon 6 Yer İstasyonu")
    window.setWindowIcon(QIcon("logo.png"))

    window.addWidget(first)
    window.addWidget(second)
    window.addWidget(third)

    window.showMaximized()

    app.exec()
