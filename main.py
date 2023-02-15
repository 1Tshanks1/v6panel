from PySide6.QtWidgets import QApplication, QStackedWidget, QWidget,QApplication,QMainWindow,QPushButton,QVBoxLayout,QHBoxLayout,QMessageBox
from PySide6.QtGui import QIcon, QPixmap, QColor, QFont, QPalette
from PySide6.QtCore import QCoreApplication
from firstpage import Ui_pageOne
from secondpage import Ui_secondPage, Ui_secondthPage, Ui_secondthirdPage
from backend import device
from serial.tools import list_ports
import sys    



xbeeDevice1 = device()
xbeeDevice2 = device()
xbeeDevice3 = device()
count = 0

app = QApplication(sys.argv)

class firstPage(QWidget,Ui_pageOne,Ui_secondPage):
    
    def __init__(self,*args):
        super().__init__()
        self.setupUi(self)
        self.xbeeDevice1 = args[0]
        self.xbeeDevice2 = args[1]
        self.xbeeDevice3 = args[2]
        self.count = 0
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
        window.setCurrentIndex(window.currentIndex() + 1)
        
     
    
    def add(self):
        global xbeeDevice1
        global xbeeDevice2
        global xbeeDevice3
        global count

        succesmsg = QMessageBox()
        succesmsg.setWindowTitle("Succesful")
        succesmsg.setText("You have succesfully connected a device.") 
        if count == 0:
            xbeeDevice1 = device(self.flightName.text(),self.deviceName.text(),self.portBox.currentText(),self.baudBox.currentText())
            count += 1
            succesmsg.exec()
        elif count == 1:
            xbeeDevice2 = device(self.flightName.text(),self.deviceName.text(),self.portBox.currentText(),self.baudBox.currentText())
            count += 1
            succesmsg.exec()
        elif count == 2:
            xbeeDevice3 = device(self.flightName.text(),self.deviceName.text(),self.portBox.currentText(),self.baudBox.currentText())
            count += 1
            succesmsg.exec()
        else:
            errormsg = QMessageBox()
            errormsg.setWindowTitle("Error")
            errormsg.setText("You have reached maximum number of devices!!\nYou cannot add a new device.") 
            errormsg.exec()
            
        
class secondPage(QWidget,Ui_secondPage,Ui_secondthPage,Ui_secondthirdPage):
    isnext = False
    isPrevious = False
    def __init__(self,*args):
        super(secondPage,self).__init__()
        if count == 0:
            self.ui = Ui_secondPage()
            self.ui.setupUi(self)
        elif count == 1:
            self.ui = Ui_secondthPage
            self.ui.setupUi(self)
        elif count == 2:
            self.ui = Ui_secondthirdPage
            self.ui.setupUi(self)
            
        # self.altitude = xbeeDevice1.altitude
        # self.longtitude = xbeeDevice1.longtitude
        # self.velocity = xbeeDevice1.velocity
        # self.latitude = xbeeDevice1.latitude

        # self.altitudeLabel.setText(QCoreApplication.translate("secondPage", u"{}", None).format())
        # self.longtitudeLabel.setText(QCoreApplication.translate("secondPage", u"{}", None).format())
        # self.velocityLabel.setText(QCoreApplication.translate("secondPage", u"{}", None).format())
        # self.latitudeLabe.setText(QCoreApplication.translate("secondPage", u"{}", None).format())

        
        # self.nextButton.clicked.connect(self.nextPage)
        # self.backButton.clicked.connect(self.previousPage)



    def nextPage(self):
        window.setCurrentIndex(window.currentIndex() + 1)
        
    
    def previousPage(self):
        window.setCurrentIndex(window.currentIndex() - 1)
        

window = QStackedWidget()
first = firstPage(xbeeDevice1,xbeeDevice2,xbeeDevice3)
second = secondPage(xbeeDevice1,xbeeDevice2,xbeeDevice3)
window.setWindowTitle("Versiyon 6 Yer İstasyonu")
window.setWindowIcon(QIcon("logo.jpeg"))

window.addWidget(first)
window.addWidget(second)

window.showMaximized()

app.exec()
