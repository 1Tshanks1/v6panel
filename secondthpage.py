# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secondthpage.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_secondthPage(object):
    def setupUi(self, secondPage):
        if not secondPage.objectName():
            secondPage.setObjectName(u"secondPage")
        secondPage.resize(960, 731)
        self.label = QLabel(secondPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 120, 151, 61))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label_2 = QLabel(secondPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 180, 151, 61))
        self.label_2.setFont(font)
        self.label_3 = QLabel(secondPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 240, 151, 61))
        self.label_3.setFont(font)
        self.label_4 = QLabel(secondPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 300, 151, 61))
        self.label_4.setFont(font)
        self.altitudeLabel = QLabel(secondPage)
        self.altitudeLabel.setObjectName(u"altitudeLabel")
        self.altitudeLabel.setGeometry(QRect(320, 240, 151, 61))
        self.altitudeLabel.setFont(font)
        self.longtitudeLabel = QLabel(secondPage)
        self.longtitudeLabel.setObjectName(u"longtitudeLabel")
        self.longtitudeLabel.setGeometry(QRect(320, 180, 151, 61))
        self.longtitudeLabel.setFont(font)
        self.velocityLabel = QLabel(secondPage)
        self.velocityLabel.setObjectName(u"velocityLabel")
        self.velocityLabel.setGeometry(QRect(320, 300, 151, 61))
        self.velocityLabel.setFont(font)
        self.latitudeLabel = QLabel(secondPage)
        self.latitudeLabel.setObjectName(u"latitudeLabel")
        self.latitudeLabel.setGeometry(QRect(320, 120, 151, 61))
        self.latitudeLabel.setFont(font)
        self.setButton = QPushButton(secondPage)
        self.setButton.setObjectName(u"setButton")
        self.setButton.setGeometry(QRect(350, 360, 81, 41))
        self.setButton.setFont(font)
        self.backButton = QPushButton(secondPage)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(290, 420, 131, 41))
        self.backButton.setFont(font)
        self.nextButton = QPushButton(secondPage)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(510, 420, 131, 41))
        self.nextButton.setFont(font)
        self.resButton = QPushButton(secondPage)
        self.resButton.setObjectName(u"resButton")
        self.resButton.setGeometry(QRect(290, 360, 61, 41))
        self.resButton.setFont(font)
        self.latitudeLabel_2 = QLabel(secondPage)
        self.latitudeLabel_2.setObjectName(u"latitudeLabel_2")
        self.latitudeLabel_2.setGeometry(QRect(520, 120, 151, 61))
        self.latitudeLabel_2.setFont(font)
        self.velocityLabel_2 = QLabel(secondPage)
        self.velocityLabel_2.setObjectName(u"velocityLabel_2")
        self.velocityLabel_2.setGeometry(QRect(520, 300, 151, 61))
        self.velocityLabel_2.setFont(font)
        self.altitudeLabel_2 = QLabel(secondPage)
        self.altitudeLabel_2.setObjectName(u"altitudeLabel_2")
        self.altitudeLabel_2.setGeometry(QRect(520, 240, 151, 61))
        self.altitudeLabel_2.setFont(font)
        self.longtitudeLabel_2 = QLabel(secondPage)
        self.longtitudeLabel_2.setObjectName(u"longtitudeLabel_2")
        self.longtitudeLabel_2.setGeometry(QRect(520, 180, 151, 61))
        self.longtitudeLabel_2.setFont(font)
        self.resButton_2 = QPushButton(secondPage)
        self.resButton_2.setObjectName(u"resButton_2")
        self.resButton_2.setGeometry(QRect(510, 370, 61, 41))
        self.resButton_2.setFont(font)
        self.setButton_2 = QPushButton(secondPage)
        self.setButton_2.setObjectName(u"setButton_2")
        self.setButton_2.setGeometry(QRect(570, 370, 81, 41))
        self.setButton_2.setFont(font)
        self.devicename1 = QLabel(secondPage)
        self.devicename1.setObjectName(u"devicename1")
        self.devicename1.setGeometry(QRect(310, 50, 151, 61))
        self.devicename1.setFont(font)
        self.devicename2 = QLabel(secondPage)
        self.devicename2.setObjectName(u"devicename2")
        self.devicename2.setGeometry(QRect(500, 50, 161, 61))
        self.devicename2.setFont(font)

        self.retranslateUi(secondPage)

        QMetaObject.connectSlotsByName(secondPage)
    # setupUi

    def retranslateUi(self, secondPage):
        secondPage.setWindowTitle(QCoreApplication.translate("secondPage", u"Form", None))
        self.label.setText(QCoreApplication.translate("secondPage", u"Latitude:", None))
        self.label_2.setText(QCoreApplication.translate("secondPage", u"Longtitude:", None))
        self.label_3.setText(QCoreApplication.translate("secondPage", u"Altitude:", None))
        self.label_4.setText(QCoreApplication.translate("secondPage", u"Velocity:", None))
        self.altitudeLabel.setText(QCoreApplication.translate("secondPage", u"Altitude", None))
        self.longtitudeLabel.setText(QCoreApplication.translate("secondPage", u"Longtitude", None))
        self.velocityLabel.setText(QCoreApplication.translate("secondPage", u"Velocity", None))
        self.latitudeLabel.setText(QCoreApplication.translate("secondPage", u"Latitude", None))
        self.setButton.setText(QCoreApplication.translate("secondPage", u"SET", None))
        self.backButton.setText(QCoreApplication.translate("secondPage", u"GO BACK", None))
        self.nextButton.setText(QCoreApplication.translate("secondPage", u"NEXT", None))
        self.resButton.setText(QCoreApplication.translate("secondPage", u"RES", None))
        self.latitudeLabel_2.setText(QCoreApplication.translate("secondPage", u"Latitude", None))
        self.velocityLabel_2.setText(QCoreApplication.translate("secondPage", u"Velocity", None))
        self.altitudeLabel_2.setText(QCoreApplication.translate("secondPage", u"Altitude", None))
        self.longtitudeLabel_2.setText(QCoreApplication.translate("secondPage", u"Longtitude", None))
        self.resButton_2.setText(QCoreApplication.translate("secondPage", u"RES", None))
        self.setButton_2.setText(QCoreApplication.translate("secondPage", u"SET", None))
        self.devicename1.setText(QCoreApplication.translate("secondPage", u"devicename1", None))
        self.devicename2.setText(QCoreApplication.translate("secondPage", u"devicename2", None))
    # retranslateUi

