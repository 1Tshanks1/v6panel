import serial
import struct
import time

ser = serial.Serial("COM6",19200,bytesize=serial.EIGHTBITS )
paketSayac = 0
data = []

class write():
    def __init__(self):
        
        if paketSayac == 256:
                paketSayac = 0
        if not ser.isOpen():
            ser.open()
        dataPacket = bytearray(78)
        dataPacket[0] = 0xFF 
        dataPacket[1] = 0xFF 
        dataPacket[2] = 0x54 
        dataPacket[3] = 0x52 
        dataPacket[4] = 0 #takım id self
        dataPacket[5] = paketSayac 
        altitude = self.remoteDevice1.altitude[-1]-self.remoteDevice1.initialAltitude 
        dataPacket[6:10] = struct.pack('@f',altitude)
        dataPacket[10:14] = struct.pack('@f', self.remoteDevice1.galtitude)
        dataPacket[14:18] = struct.pack('@f', self.remoteDevice1.loc[-1][0])
        dataPacket[18:22] = struct.pack('@f', self.remoteDevice1.loc[-1][1])
        if self.count == 2:
            dataPacket[22:26] = struct.pack('@f', self.remoteDevice2.altitude[-1])
            dataPacket[26:30] = struct.pack('@f', self.remoteDevice2.loc[-1][0])
            dataPacket[30:34] = struct.pack('@f', self.remoteDevice2.loc[-1][1])
        dataPacket[74] = self.remoteDevice1.stat
        temp = dataPacket[5:76]
        dataPacket[75] = int(sum(temp)%256)
        dataPacket[76] = 0x0D
        dataPacket[77] = 0x0A
        finalDataPacket = bytes.fromhex(dataPacket[:39].hex())+dataPacket[39:]
        ser.write(finalDataPacket)

        print(repr(dataPacket).replace('\\x', ''))

        ser.close()
        paketSayac+=1   