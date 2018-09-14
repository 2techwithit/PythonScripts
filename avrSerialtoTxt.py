import os
import serial
import datetime

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

dataTxt = 'testData2.txt'
txtTrue = os.path.isfile(dataDir+'\\'+dataTxt)

print(txtTrue)

if txtTrue == True:
    print('Data File Exists')
    editData = open(dataTxt, 'a')
else:
    editData = open(dataTxt, 'w+')
    print('Creating File' + dataTxt)

editData.write('\n'+str(writeTime)+'\n')

avrIn = serial.Serial('COM3')
avrIn.flushInput()

while True:
    try:
        serData = avrIn.readline()
        decodeIn = int(serData[0:len(serData)-2].decode('utf-8'))
        editData.write(str(decodeIn)+',')
        print(str(decodeIn))
    except:
        print('Keyboard Interrupt')
        avrIn.flushInput()
        avrIn.close()
        break

editData.close()
print('File Saved')
