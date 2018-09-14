import os
import serial
import datetime
import csv

ser = serial.Serial('COM3', 9600, timeout =2)
ser.flushInput()

if ser.is_open is False:
    print('Serial port is not open!')
else:
    print('Connected to serial port.')

cWrkDir = os.getcwd()
dataDir = r'C:\\Users\t3ch1t\Documents\Python'
writeTime = datetime.datetime.now()
print(cWrkDir)

if cWrkDir != dataDir:
    os.chdir(dataDir)
    cWrkDir = os.getcwd()
    print(cWrkDir)
else:
    print(cWrkDir)

dataCSV = 'dataTest.csv'

with open(dataCSV, 'a', newline='') as csvfile:
    editCSV = csv.writer(csvfile)
    editCSV.writerow([writeTime])
    while True:
        try:
            serData = ser.readline()
            decodeIn = int(serData[0:len(serData)-2].decode('utf-8'))
            dataDelim = str(decodeIn+',')
            editCSV.writerow([dataDelim])
        except:
            print('Keyboard Interrupt')
            break

ser.flushInput()
ser.close()
print('Serial Closed')

