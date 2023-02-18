
import time
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress
import serial
import time



x = XBeeDevice("COM4", 57600)
y = RemoteXBeeDevice(x, "0013A2004175CAE6")
x.open()

print(x.get_64bit_addr())
while True:

    comingData = x.read_data_from(y)
    if comingData != None:
        seperatedData = comingData.data.decode(
            'utf8', 'strict').split(",")
        print(seperatedData)
        time.sleep(0.1)
