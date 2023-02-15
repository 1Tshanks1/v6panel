# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'firstpage.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_pageOne(object):
    def setupUi(self, pageOne):
        if not pageOne.objectName():
            pageOne.setObjectName(u"pageOne")
        pageOne.resize(752, 643)
        self.label = QLabel(pageOne)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 150, 151, 31))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label_2 = QLabel(pageOne)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 200, 161, 31))
        self.label_2.setFont(font)
        self.label_3 = QLabel(pageOne)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 290, 131, 31))
        self.label_3.setFont(font)
        self.label_4 = QLabel(pageOne)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 250, 131, 31))
        self.label_4.setFont(font)
        self.baudBox = QComboBox(pageOne)
        self.baudBox.addItem("")
        self.baudBox.addItem("")
        self.baudBox.addItem("")
        self.baudBox.addItem("")
        self.baudBox.addItem("")
        self.baudBox.addItem("")
        self.baudBox.addItem("")
        self.baudBox.setObjectName(u"baudBox")
        self.baudBox.setGeometry(QRect(330, 290, 131, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.baudBox.setFont(font1)
        self.deviceName = QLineEdit(pageOne)
        self.deviceName.setObjectName(u"deviceName")
        self.deviceName.setGeometry(QRect(330, 200, 131, 31))
        self.flightName = QLineEdit(pageOne)
        self.flightName.setObjectName(u"flightName")
        self.flightName.setGeometry(QRect(330, 150, 131, 31))
        self.portBox = QComboBox(pageOne)
        self.portBox.setObjectName(u"portBox")
        self.portBox.setGeometry(QRect(330, 250, 131, 31))
        self.portBox.setFont(font1)
        self.addButton = QPushButton(pageOne)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(160, 340, 141, 51))
        self.addButton.setFont(font)
        self.nextButton = QPushButton(pageOne)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(320, 340, 141, 51))
        self.nextButton.setFont(font)
        self.reloadButton = QPushButton(pageOne)
        self.reloadButton.setObjectName(u"reloadButton")
        self.reloadButton.setGeometry(QRect(220, 252, 41, 31))
        self.reloadButton.setStyleSheet(u"background-image:url(:/reload.png);\n"
"background-repeat: none;")

        self.retranslateUi(pageOne)

        QMetaObject.connectSlotsByName(pageOne)
    # setupUi

    def retranslateUi(self, pageOne):
        pageOne.setWindowTitle(QCoreApplication.translate("pageOne", u"Form", None))
        self.label.setText(QCoreApplication.translate("pageOne", u"Flight Name", None))
        self.label_2.setText(QCoreApplication.translate("pageOne", u"Device Name", None))
        self.label_3.setText(QCoreApplication.translate("pageOne", u"Baudrate", None))
        self.label_4.setText(QCoreApplication.translate("pageOne", u"Port", None))
        self.baudBox.setItemText(0, QCoreApplication.translate("pageOne", u"2400", None))
        self.baudBox.setItemText(1, QCoreApplication.translate("pageOne", u"4800", None))
        self.baudBox.setItemText(2, QCoreApplication.translate("pageOne", u"9600", None))
        self.baudBox.setItemText(3, QCoreApplication.translate("pageOne", u"19200", None))
        self.baudBox.setItemText(4, QCoreApplication.translate("pageOne", u"28800", None))
        self.baudBox.setItemText(5, QCoreApplication.translate("pageOne", u"38400", None))
        self.baudBox.setItemText(6, QCoreApplication.translate("pageOne", u"57600", None))

        self.addButton.setText(QCoreApplication.translate("pageOne", u"ADD", None))
        self.nextButton.setText(QCoreApplication.translate("pageOne", u"NEXT", None))
        self.reloadButton.setText("")
    # retranslateUi

