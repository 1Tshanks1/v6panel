from digi.xbee.devices import XBeeDevice,RemoteXBeeDevice, XBee64BitAddress
import serial
import time
import os
import sqlite3

class device():

    #   flightname , name, com, baudrate
    def __init__(self, *args):
        if len(args) == 4 and len(args[0]) > 0 and len(args[1]) > 0:
            self = XBeeDevice(args[2], int(args[3]))
            self.name = args[1]
            self.flightname = args[0]
            self.open()
            self.isTrue = True
            self.readData()
            print("BAŞARILI")
        else:
            pass


    def readData(self):
        if self.isTrue:
            comingData = self.read_data()
            if comingData!= None:
                seperatedData = comingData.data.decode('utf8', 'strict').split(",")
                self.latitude = seperatedData[0]
                self.longtitude = seperatedData[1]
                self.velocity = seperatedData[2]
                self.altitude = seperatedData[3]
                time.sleep(0.1)
            return self.latitude,self.longtitude,self.velocity,self.altitude, device.readData(self.isTrue)
        else:
            return


    def writeData(self):
        conn = sqlite3.connect('flights')

        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS ?(
                latitude real,
                longtidude real,
                altitude real,
                velocity real)"""),(self.flightname)

        c.execute("""INSERT INTO flights VALUES(?,?,?,?)""",(self.latitude,self.longtitude,self.altitude,self.velocity))

        conn.commit()

        print(c.fetchall())

        conn.close() 


        

