from PySide6.QtWidgets import QApplication, QStackedWidget, QWidget, QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide6.QtGui import QIcon, QPixmap, QColor, QFont, QPalette
from PySide6.QtCore import QCoreApplication
from firstpage import Ui_pageOne
from secondpage import Ui_secondPage, Ui_secondthPage, Ui_secondthirdPage
from backend import device
from serial.tools import list_ports
import sys


xbeeDevice1 = None
xbeeDevice2 = None
xbeeDevice3 = None
count = 0


class firstPage(QWidget, Ui_pageOne, Ui_secondPage):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.scanComs()
        self.reloadButton.clicked.connect(self.scanComs)
        self.nextButton.clicked.connect(self.nextPage)
        self.addButton.clicked.connect(self.add)

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
        elif count == 2:
            window.setCurrentIndex(window.currentIndex() + 2)
        elif count == 3:
            window.setCurrentIndex(window.currentIndex() + 2)

    def add(self):
        global xbeeDevice1
        global xbeeDevice2
        global xbeeDevice3
        global count

        succesmsg = QMessageBox()
        succesmsg.setWindowTitle("Succesful")
        succesmsg.setText("You have succesfully connected a device.")
        errormsgsec = QMessageBox()
        errormsgsec.setWindowTitle("Error")
        errormsgsec.setText(
            "Flight name and Device name have to be longer than 1 character!!")
        if count == 0 and len(self.flightName.text()) > 0 and len(self.deviceName.text()) > 0:

            xbeeDevice1 = device(self.flightName.text(), self.deviceName.text(
            ), self.portBox.currentText(), self.baudBox.currentText())
            count += 1
            succesmsg.exec()
        elif count == 1 and len(self.flightName.text()) > 0 and len(self.deviceName.text()) > 0:
            xbeeDevice2 = device(self.flightName.text(), self.deviceName.text(
            ), self.portBox.currentText(), self.baudBox.currentText())
            count += 1
            succesmsg.exec()
        elif count == 2 and len(self.flightName.text()) > 0 and len(self.deviceName.text()) > 0:
            xbeeDevice3 = device(self.flightName.text(), self.deviceName.text(
            ), self.portBox.currentText(), self.baudBox.currentText())
            count += 1
            succesmsg.exec()
        elif len(self.flightName.text()) == 0 or len(self.deviceName.text()) == 0:
            errormsgsec.exec()

        else:
            errormsg = QMessageBox()
            errormsg.setWindowTitle("Error")
            errormsg.setText(
                "You have reached maximum number of devices!!\nYou cannot add a new device.")
            errormsg.exec()


class secondPage(QWidget, Ui_secondPage):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.nextButton.clicked.connect(self.nextPage)
        self.backButton.clicked.connect(self.previousPage)
        self.resButton.clicked.connect(self.getData)
        self.setButton.clicked.connect(self.setData)

    def setData(self):
        xbeeDevice1.initialLatitude = xbeeDevice1.latitude
        xbeeDevice1.initialLongtitude = xbeeDevice1.longtitude
        xbeeDevice1.initialAltitude = xbeeDevice1.altitude
        xbeeDevice1.initialVelocity = xbeeDevice1.velocity
        print(xbeeDevice1.initialLatitude)
        print(xbeeDevice1.initialLongtitude)
        print(xbeeDevice1.initialAltitude)
        print(xbeeDevice1.initialVelocity)

    def getData(self):
        xbeeDevice1.readData()
        self.altitudeLabel.setText(xbeeDevice1.altitude)
        self.longtitudeLabel.setText(xbeeDevice1.longtitude)
        self.velocityLabel.setText(xbeeDevice1.velocity)
        self.latitudeLabe.setText(xbeeDevice1.latitude)

    def nextPage(self):
        window.setCurrentIndex(window.currentIndex() + 3)

    def previousPage(self):
        window.setCurrentIndex(window.currentIndex() - 1)


class secondthPage(QWidget, Ui_secondthPage):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.nextButton.clicked.connect(self.nextPage)
        self.backButton.clicked.connect(self.previousPage)
        self.resButton.clicked.connect(self.getData)
        self.setButton.clicked.connect(self.setData)
        self.nextButton.clicked.connect(self.nextPage)
        self.backButton.clicked.connect(self.previousPage)

    def setData(self):
        xbeeDevice1.initialLatitude = xbeeDevice1.latitude
        xbeeDevice1.initialLongtitude = xbeeDevice1.longtitude
        xbeeDevice1.initialAltitude = xbeeDevice1.altitude
        xbeeDevice1.initialVelocity = xbeeDevice1.velocity
        xbeeDevice2.initialLatitude = xbeeDevice2.latitude
        xbeeDevice2.initialLongtitude = xbeeDevice2.longtitude
        xbeeDevice2.initialAltitude = xbeeDevice2.altitude
        xbeeDevice2.initialVelocity = xbeeDevice2.velocity

    def getData(self):
        xbeeDevice1.readData()
        self.altitudeLabel.setText(xbeeDevice1.altitude)
        self.longtitudeLabel.setText(xbeeDevice1.longtitude)
        self.velocityLabel.setText(xbeeDevice1.velocity)
        self.latitudeLabel.setText(xbeeDevice1.latitude)
        xbeeDevice2.readData()
        self.altitudeLabel_2.setText(xbeeDevice2.altitude)
        self.longtitudeLabel_2.setText(xbeeDevice2.longtitude)
        self.velocityLabel_2.setText(xbeeDevice2.velocity)
        self.latitudeLabel_2.setText(xbeeDevice2.latitude)

    def nextPage(self):
        window.setCurrentIndex(window.currentIndex() + 2)

    def previousPage(self):
        window.setCurrentIndex(window.currentIndex() - 2)


class secondthirdPage(QWidget, Ui_secondthirdPage):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.nextButton.clicked.connect(self.nextPage)
        self.backButton.clicked.connect(self.previousPage)
        self.resButton.clicked.connect(self.getData)
        self.setButton.clicked.connect(self.setData)
        self.nextButton.clicked.connect(self.nextPage)
        self.backButton.clicked.connect(self.previousPage)

    def setData(self):
        xbeeDevice1.initialLatitude = xbeeDevice1.latitude
        xbeeDevice1.initialLongtitude = xbeeDevice1.longtitude
        xbeeDevice1.initialAltitude = xbeeDevice1.altitude
        xbeeDevice1.initialVelocity = xbeeDevice1.velocity
        xbeeDevice2.initialLatitude = xbeeDevice2.latitude
        xbeeDevice2.initialLongtitude = xbeeDevice2.longtitude
        xbeeDevice2.initialAltitude = xbeeDevice2.altitude
        xbeeDevice2.initialVelocity = xbeeDevice2.velocity
        xbeeDevice3.initialLatitude = xbeeDevice3.latitude
        xbeeDevice3.initialLongtitude = xbeeDevice3.longtitude
        xbeeDevice3.initialAltitude = xbeeDevice3.altitude
        xbeeDevice3.initialVelocity = xbeeDevice3.velocity

    def getData(self):
        xbeeDevice1.readData()
        self.altitudeLabel.setText(xbeeDevice1.altitude)
        self.longtitudeLabel.setText(xbeeDevice1.longtitude)
        self.velocityLabel.setText(xbeeDevice1.velocity)
        self.latitudeLabel.setText(xbeeDevice1.latitude)
        xbeeDevice2.readData()
        self.altitudeLabel_2.setText(xbeeDevice2.altitude)
        self.longtitudeLabel_2.setText(xbeeDevice2.longtitude)
        self.velocityLabel_2.setText(xbeeDevice2.velocity)
        self.latitudeLabel_2.setText(xbeeDevice2.latitude)
        xbeeDevice3.readData()
        self.altitudeLabel_3.setText(xbeeDevice3.altitude)
        self.longtitudeLabel_3.setText(xbeeDevice3.longtitude)
        self.velocityLabel_3.setText(xbeeDevice3.velocity)
        self.latitudeLabel_3.setText(xbeeDevice3.latitude)

    def nextPage(self):
        window.setCurrentIndex(window.currentIndex() + 1)

    def previousPage(self):
        window.setCurrentIndex(window.currentIndex() - 3)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = QStackedWidget()
    first = firstPage()
    second = secondPage()
    secondth = secondthPage()
    secondthird = secondthirdPage()
    window.setWindowTitle("Versiyon 6 Yer İstasyonu")
    window.setWindowIcon(QIcon("logo.jpeg"))

    window.addWidget(first)
    window.addWidget(second)
    window.addWidget(secondth)
    window.addWidget(secondthird)

    window.showMaximized()

    app.exec()
