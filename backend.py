from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress
import serial
import time
import os
import sqlite3
import struct
import random



class device():

    #   flightname , name, com, baudrate
    def __init__(self, *args):

        self.device = XBeeDevice(args[2], int(args[3]))
        self.name = args[1]
        self.flightname = args[0]

        self.device.open()
        self.isTrue = True
        self.count = 0

        print("BAŞARILI")

    def createRemoteDevice(self, deviceAdress):
        if self.count == 0:
            self.remoteDevice1 = RemoteXBeeDevice(
                self.device, XBee64BitAddress.from_hex_string(deviceAdress))
            self.remoteDevice1.loc = []
            self.remoteDevice1.velocity = []
            self.remoteDevice1.altitude = []
            self.remoteDevice1.initialAltitude = 0
        if self.count == 1:
            self.remoteDevice2 = RemoteXBeeDevice(
                self.device, XBee64BitAddress.from_hex_string(deviceAdress))
            self.remoteDevice2.loc = []
            self.remoteDevice2.velocity = []
            self.remoteDevice2.altitude = []
            self.remoteDevice1.initialAltitude = 0
        self.count += 1

    def clear(self):
        self.remoteDevice1.altitude.clear()
        self.remoteDevice1.loc.clear()
        self.remoteDevice1.velocity.clear()

        if self.count == 2:
            self.remoteDevice2.altitude.clear()
            self.remoteDevice2.loc.clear()
            self.remoteDevice2.velocity.clear()

    def readData(self, remoteDevice):
        global ser, paketSayac
        comingData = self.device.read_data_from(remoteDevice)
        if comingData != None:
            seperatedData = comingData.data.decode(
                'utf8', 'strict').split(",")
        remoteDevice.loc.append(
            [float(seperatedData[0]),float(seperatedData[1])])
        remoteDevice.velocity.append(float(seperatedData[2]))
        remoteDevice.altitude.append(float(seperatedData[3]))
        remoteDevice.stat = bool(seperatedData[4])
        remoteDevice.galtitude = float(seperatedData[5]) 

        time.sleep(0.1)

    def writeData(self):
        conn = sqlite3.connect('flights')

        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS ?(
                latitude real,
                longtidude real,
                altitude real,
                velocity real)"""), (self.flightname)

        c.execute("""INSERT INTO flights VALUES(?,?,?,?)""",
                  (self.latitude, self.longtitude, self.altitude, self.velocity))

        conn.commit()

        print(c.fetchall())

        conn.close()
    def readFromDB():
        pass


