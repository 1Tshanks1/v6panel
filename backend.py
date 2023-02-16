from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress
import serial
import time
import os
import sqlite3
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import queue
import numpy as np



class device():

    #   flightname , name, com, baudrate
    def __init__(self, *args):

        self.device = XBeeDevice(args[2], int(args[3]))
        self.name = args[1]
        self.flightname = args[0]

        self.device.open()
        self.isTrue = True
        self.count = 0
        device.readData(self, args[2], args[3])
        print("BAŞARILI")

    def createRemoteDevice(self, deviceAdress):
        if self.count == 0:
            self.remoteDevice1 = RemoteXBeeDevice(self.device, deviceAdress)
            self.count += 1
            self.remoteDevice1.latitude = []
            self.remoteDevice1.longtitude = []
            self.remoteDevice1.velocity = []
            self.remoteDevice1.altitude = []
        if self.count == 1:
            self.remoteDevice2 = RemoteXBeeDevice(self.device, deviceAdress)
            self.remoteDevice2.latitude = []
            self.remoteDevice2.longtitude = []
            self.remoteDevice2.velocity = []
            self.remoteDevice2.altitude = []
            self.count += 1

    def readData(self, remoteDevice):

        comingData = self.device.read_data_from(self.device, remoteDevice)
        if comingData != None:
            seperatedData = comingData.data.decode(
                'utf8', 'strict').split(",")
            remoteDevice.latitude.append(seperatedData[0])
            remoteDevice.longtitude.append(seperatedData[1])
            remoteDevice.velocity.append(seperatedData[2])
            remoteDevice.altitude.append(seperatedData[3])
            time.sleep(0.1)

    def writeData(self):
        conn = sqlite3.connect('flights')

        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS ?(
                latitude real,
                longtidude real,
                altitude real,
                velocity real)"""), (self.flightname)

       # c.execute("""INSERT INTO flights VALUES(?,?,?,?)""",
                  #(self.latitude, self.longtitude, self.altitude, self.velocity))

        conn.commit()

        print(c.fetchall())

        conn.close()
