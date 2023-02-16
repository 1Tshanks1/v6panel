# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'thirdpage.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

from pyqtgraph import PlotWidget

class Ui_thirdPage(object):
    def setupUi(self, thirdPage):
        if not thirdPage.objectName():
            thirdPage.setObjectName(u"thirdPage")
        thirdPage.resize(1177, 710)
        self.gridLayout_6 = QGridLayout(thirdPage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(thirdPage)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.remoteDeviceName = QLabel(thirdPage)
        self.remoteDeviceName.setObjectName(u"remoteDeviceName")
        self.remoteDeviceName.setFont(font)

        self.gridLayout_2.addWidget(self.remoteDeviceName, 0, 1, 1, 1)

        self.remoteDeviceName2 = QLabel(thirdPage)
        self.remoteDeviceName2.setObjectName(u"remoteDeviceName2")
        self.remoteDeviceName2.setFont(font)

        self.gridLayout_2.addWidget(self.remoteDeviceName2, 0, 2, 1, 1)

        self.latitude = QLabel(thirdPage)
        self.latitude.setObjectName(u"latitude")
        self.latitude.setFont(font)

        self.gridLayout_2.addWidget(self.latitude, 1, 0, 1, 1)

        self.remoteDeviceLatitude = QLabel(thirdPage)
        self.remoteDeviceLatitude.setObjectName(u"remoteDeviceLatitude")
        self.remoteDeviceLatitude.setFont(font)

        self.gridLayout_2.addWidget(self.remoteDeviceLatitude, 1, 1, 1, 1)

        self.remoteDevice2Latitude = QLabel(thirdPage)
        self.remoteDevice2Latitude.setObjectName(u"remoteDevice2Latitude")
        self.remoteDevice2Latitude.setFont(font)

        self.gridLayout_2.addWidget(self.remoteDevice2Latitude, 1, 2, 1, 1)

        self.longtitude = QLabel(thirdPage)
        self.longtitude.setObjectName(u"longtitude")
        self.longtitude.setFont(font)

        self.gridLayout_2.addWidget(self.longtitude, 2, 0, 1, 1)

        self.remoteDeviceLongtitude = QLabel(thirdPage)
        self.remoteDeviceLongtitude.setObjectName(u"remoteDeviceLongtitude")
        self.remoteDeviceLongtitude.setFont(font)

        self.gridLayout_2.addWidget(self.remoteDeviceLongtitude, 2, 1, 1, 1)

        self.remoteDevice2Longtitude = QLabel(thirdPage)
        self.remoteDevice2Longtitude.setObjectName(u"remoteDevice2Longtitude")
        self.remoteDevice2Longtitude.setFont(font)

        self.gridLayout_2.addWidget(self.remoteDevice2Longtitude, 2, 2, 1, 1)

        self.altitude = QLabel(thirdPage)
        self.altitude.setObjectName(u"altitude")
        self.altitude.setFont(font)

        self.gridLayout_2.addWidget(self.altitude, 3, 0, 1, 1)

        self.remoteDeviceAltitude = QLabel(thirdPage)
        self.remoteDeviceAltitude.setObjectName(u"remoteDeviceAltitude")
        self.remoteDeviceAltitude.setFont(font)

        self.gridLayout_2.addWidget(self.remoteDeviceAltitude, 3, 1, 1, 1)

        self.remoteDevice2Altitude = QLabel(thirdPage)
        self.remoteDevice2Altitude.setObjectName(u"remoteDevice2Altitude")
        self.remoteDevice2Altitude.setFont(font)

        self.gridLayout_2.addWidget(self.remoteDevice2Altitude, 3, 2, 1, 1)

        self.velocity = QLabel(thirdPage)
        self.velocity.setObjectName(u"velocity")
        self.velocity.setFont(font)

        self.gridLayout_2.addWidget(self.velocity, 4, 0, 1, 1)

        self.remoteDeviceVelocity = QLabel(thirdPage)
        self.remoteDeviceVelocity.setObjectName(u"remoteDeviceVelocity")
        self.remoteDeviceVelocity.setFont(font)

        self.gridLayout_2.addWidget(self.remoteDeviceVelocity, 4, 1, 1, 1)

        self.remoteDevice2Velocity = QLabel(thirdPage)
        self.remoteDevice2Velocity.setObjectName(u"remoteDevice2Velocity")
        self.remoteDevice2Velocity.setFont(font)

        self.gridLayout_2.addWidget(self.remoteDevice2Velocity, 4, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.device1VT = PlotWidget(thirdPage)
        self.device1VT.setObjectName(u"device1VT")

        self.gridLayout.addWidget(self.device1VT, 1, 0, 1, 1)

        self.remoteDeviceName2_2 = QLabel(thirdPage)
        self.remoteDeviceName2_2.setObjectName(u"remoteDeviceName2_2")
        self.remoteDeviceName2_2.setFont(font)

        self.gridLayout.addWidget(self.remoteDeviceName2_2, 0, 1, 1, 1)

        self.remoteDeviceName_1 = QLabel(thirdPage)
        self.remoteDeviceName_1.setObjectName(u"remoteDeviceName_1")
        self.remoteDeviceName_1.setFont(font)

        self.gridLayout.addWidget(self.remoteDeviceName_1, 0, 0, 1, 1)

        self.device1AT = PlotWidget(thirdPage)
        self.device1AT.setObjectName(u"device1AT")

        self.gridLayout.addWidget(self.device1AT, 2, 0, 1, 1)

        self.device2AT = PlotWidget(thirdPage)
        self.device2AT.setObjectName(u"device2AT")

        self.gridLayout.addWidget(self.device2AT, 2, 1, 1, 1)

        self.device2VT = PlotWidget(thirdPage)
        self.device2VT.setObjectName(u"device2VT")

        self.gridLayout.addWidget(self.device2VT, 1, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 1, 2, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.backButton = QPushButton(thirdPage)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setFont(font)

        self.gridLayout_3.addWidget(self.backButton, 0, 0, 1, 1)

        self.nextButton = QPushButton(thirdPage)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setFont(font)

        self.gridLayout_3.addWidget(self.nextButton, 0, 2, 1, 1)

        self.startButton = QPushButton(thirdPage)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setFont(font)

        self.gridLayout_3.addWidget(self.startButton, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(1128, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.retranslateUi(thirdPage)

        QMetaObject.connectSlotsByName(thirdPage)
    # setupUi

    def retranslateUi(self, thirdPage):
        thirdPage.setWindowTitle(QCoreApplication.translate("thirdPage", u"Form", None))
        self.label.setText(QCoreApplication.translate("thirdPage", u"LIVE DATA", None))
        self.remoteDeviceName.setText(QCoreApplication.translate("thirdPage", u"Device Name", None))
        self.remoteDeviceName2.setText(QCoreApplication.translate("thirdPage", u"Device Name", None))
        self.latitude.setText(QCoreApplication.translate("thirdPage", u"Latitude", None))
        self.remoteDeviceLatitude.setText(QCoreApplication.translate("thirdPage", u"Latitude", None))
        self.remoteDevice2Latitude.setText(QCoreApplication.translate("thirdPage", u"Latitude", None))
        self.longtitude.setText(QCoreApplication.translate("thirdPage", u"Longtitude", None))
        self.remoteDeviceLongtitude.setText(QCoreApplication.translate("thirdPage", u"Longtitude", None))
        self.remoteDevice2Longtitude.setText(QCoreApplication.translate("thirdPage", u"Longtitude", None))
        self.altitude.setText(QCoreApplication.translate("thirdPage", u"Altitude", None))
        self.remoteDeviceAltitude.setText(QCoreApplication.translate("thirdPage", u"Altitude", None))
        self.remoteDevice2Altitude.setText(QCoreApplication.translate("thirdPage", u"Altitude", None))
        self.velocity.setText(QCoreApplication.translate("thirdPage", u"Velocity", None))
        self.remoteDeviceVelocity.setText(QCoreApplication.translate("thirdPage", u"Velocity", None))
        self.remoteDevice2Velocity.setText(QCoreApplication.translate("thirdPage", u"Velocity", None))
        self.remoteDeviceName2_2.setText(QCoreApplication.translate("thirdPage", u"Device Name", None))
        self.remoteDeviceName_1.setText(QCoreApplication.translate("thirdPage", u"Device Name", None))
        self.backButton.setText(QCoreApplication.translate("thirdPage", u"BACK", None))
        self.nextButton.setText(QCoreApplication.translate("thirdPage", u"Next", None))
        self.startButton.setText(QCoreApplication.translate("thirdPage", u"Start", None))
    # retranslateUi

