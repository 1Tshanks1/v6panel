import serial
import time
import random
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress

x = XBeeDevice("COM3",115200)
x.open()
while True:
    comingData = x.read_data()
    if comingData != None:
        seperatedData = comingData.data.decode(
        'utf8', 'strict').split(",")
        print(seperatedData)

    time.sleep(0.1)
    