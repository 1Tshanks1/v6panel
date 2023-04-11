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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_pageOne(object):
    def setupUi(self, pageOne):
        if not pageOne.objectName():
            pageOne.setObjectName(u"pageOne")
        pageOne.resize(1009, 849)
        self.gridLayout_9 = QGridLayout(pageOne)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer = QSpacerItem(698, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(pageOne)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.flightName = QLineEdit(pageOne)
        self.flightName.setObjectName(u"flightName")

        self.gridLayout.addWidget(self.flightName, 0, 1, 1, 1)

        self.label_2 = QLabel(pageOne)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.deviceName = QLineEdit(pageOne)
        self.deviceName.setObjectName(u"deviceName")

        self.gridLayout.addWidget(self.deviceName, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_4 = QLabel(pageOne)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.reloadButton = QPushButton(pageOne)
        self.reloadButton.setObjectName(u"reloadButton")
        self.reloadButton.setStyleSheet(u"background-image:url(:/reload.png);\n"
"background-repeat: none;")

        self.gridLayout_6.addWidget(self.reloadButton, 0, 1, 1, 1)

        self.portBox = QComboBox(pageOne)
        self.portBox.setObjectName(u"portBox")
        font1 = QFont()
        font1.setPointSize(16)
        self.portBox.setFont(font1)

        self.gridLayout_6.addWidget(self.portBox, 0, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_6)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_3 = QLabel(pageOne)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.baudBox = QComboBox(pageOne)
        self.baudBox.addItem("")
        self.baudBox.addItem("")
        self.baudBox.addItem("")
        self.baudBox.addItem("")
        self.baudBox.addItem("")
        self.baudBox.addItem("")
        self.baudBox.addItem("")
        self.baudBox.addItem("")
        self.baudBox.setObjectName(u"baudBox")
        self.baudBox.setFont(font1)

        self.gridLayout_5.addWidget(self.baudBox, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_5)


        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(pageOne)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.remoteDeviceName = QLineEdit(pageOne)
        self.remoteDeviceName.setObjectName(u"remoteDeviceName")

        self.gridLayout_2.addWidget(self.remoteDeviceName, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(pageOne)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout.addWidget(self.label_5)

        self.remoteDeviceAdress = QLineEdit(pageOne)
        self.remoteDeviceAdress.setObjectName(u"remoteDeviceAdress")

        self.verticalLayout.addWidget(self.remoteDeviceAdress)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.localBox = QComboBox(pageOne)
        self.localBox.setObjectName(u"localBox")
        self.localBox.setFont(font1)

        self.gridLayout_3.addWidget(self.localBox, 0, 1, 1, 1)

        self.label_6 = QLabel(pageOne)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.gridLayout_7.addLayout(self.verticalLayout_3, 0, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.addButton = QPushButton(pageOne)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setFont(font)

        self.gridLayout_4.addWidget(self.addButton, 0, 0, 1, 1)

        self.nextButton = QPushButton(pageOne)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setFont(font)

        self.gridLayout_4.addWidget(self.nextButton, 0, 1, 1, 1)

        self.remoteDeviceAddButton = QPushButton(pageOne)
        self.remoteDeviceAddButton.setObjectName(u"remoteDeviceAddButton")
        self.remoteDeviceAddButton.setFont(font)

        self.gridLayout_4.addWidget(self.remoteDeviceAddButton, 0, 2, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_4, 1, 0, 1, 2)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.baudBox.raise_()
        self.deviceName.raise_()
        self.portBox.raise_()
        self.addButton.raise_()
        self.nextButton.raise_()
        self.reloadButton.raise_()
        self.label_5.raise_()
        self.remoteDeviceAdress.raise_()
        self.label_6.raise_()
        self.localBox.raise_()
        self.remoteDeviceAddButton.raise_()
        self.label_7.raise_()
        self.remoteDeviceName.raise_()
        self.flightName.raise_()

        self.retranslateUi(pageOne)

        QMetaObject.connectSlotsByName(pageOne)
    # setupUi

    def retranslateUi(self, pageOne):
        pageOne.setWindowTitle(QCoreApplication.translate("pageOne", u"Form", None))
        self.label.setText(QCoreApplication.translate("pageOne", u"Flight Name", None))
        self.label_2.setText(QCoreApplication.translate("pageOne", u"Device Name", None))
        self.label_4.setText(QCoreApplication.translate("pageOne", u"Port", None))
        self.reloadButton.setText("")
        self.label_3.setText(QCoreApplication.translate("pageOne", u"Baudrate", None))
        self.baudBox.setItemText(0, QCoreApplication.translate("pageOne", u"2400", None))
        self.baudBox.setItemText(1, QCoreApplication.translate("pageOne", u"4800", None))
        self.baudBox.setItemText(2, QCoreApplication.translate("pageOne", u"9600", None))
        self.baudBox.setItemText(3, QCoreApplication.translate("pageOne", u"19200", None))
        self.baudBox.setItemText(4, QCoreApplication.translate("pageOne", u"28800", None))
        self.baudBox.setItemText(5, QCoreApplication.translate("pageOne", u"38400", None))
        self.baudBox.setItemText(6, QCoreApplication.translate("pageOne", u"57600", None))
        self.baudBox.setItemText(7, QCoreApplication.translate("pageOne", u"115200", None))

        self.label_7.setText(QCoreApplication.translate("pageOne", u"Remote Device Name", None))
        self.label_5.setText(QCoreApplication.translate("pageOne", u"Remote Device 64Bit Adress", None))
        self.label_6.setText(QCoreApplication.translate("pageOne", u"Local Device", None))
        self.addButton.setText(QCoreApplication.translate("pageOne", u"ADD Local Device", None))
        self.nextButton.setText(QCoreApplication.translate("pageOne", u"NEXT", None))
        self.remoteDeviceAddButton.setText(QCoreApplication.translate("pageOne", u"ADD Remote Device", None))
    # retranslateUi

