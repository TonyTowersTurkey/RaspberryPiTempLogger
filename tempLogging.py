

####please dont't!/usr/bin/python3


import gspread #google spread sheets
import random
import time
import Adafruit_DHT #temp reading library DHT22 pin 7 logigal pin4
import pytz  #python time zones 
import kasa #Kasa highjaking library
import asyncio #also Kasa highjacking library
from datetime import datetime

''' this took a lot longer than expected.'''

#kasa smart home set up
fanAuto= kasa.SmartPlug('192.168.0.76')
temperature = 0
lTemp = 21
hTemp = 22

def fanSwitch(temperature):
    asyncio.run(fanAuto.update())
    if temperature < lTemp:
        asyncio.run(fanAuto.turn_off())

    elif temperature > hTemp:
        asyncio.run(fanAuto.turn_on())




# google sheets authentication and loading worksheet in file.
gs = gspread.service_account(filename='/home/pi/.config/gspread/service_account.json')
sh = gs.open("TemperatureLogging")
worksheet = sh.sheet1
# gets value form a single cell
# for now the place where the last updated cell is in "C2"
lastUpdatedCell = 0
timeStamp = 0
temperatureOffset = -2
while True:
    # getting now
    now = datetime.now(tz=pytz.utc)
    denverNow = now.astimezone(pytz.timezone('US/Mountain'))

    #running whenever minutes is divisible by 5
    minutes = int(denverNow.strftime('%M'))
    seconds = int(denverNow.strftime('%S'))
    if minutes % 5 == 0 :

        # getting temperature reading
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        humidity = '%.2f' % (humidity)
        temperature = '%.2f' % (temperature)
        temperature = str(int(float(temperature) + temperatureOffset))
        fanSwitch(int(temperature))
        # get last updated value
        lucplace = 'D2'
        lastUpdatedCell = worksheet.acell(lucplace).value
        lastUpdatedCell = int(lastUpdatedCell) + 1
        lastUpdatedCell = str(lastUpdatedCell)

        '''update cells'''
        worksheet.update('A' + lastUpdatedCell, str(denverNow.date()))  # u$
        worksheet.update('B' + lastUpdatedCell,
                         str(denverNow.strftime('%H:%M')))  # u$
        worksheet.update('C' + lastUpdatedCell, temperature)  # u$
        # print what has been done
        print('added' + str(denverNow.date()) + ' and ' + temperature)

        # update last updated cell
        worksheet.update(lucplace, lastUpdatedCell)
        #sleep so it does not update more than once 
        time.sleep(60)

    else:
        # sleeping
        sleepTime = 25
        print ('sleeping for ' + str(sleepTime) + ' seconds')
        time.sleep(sleepTime) # 300 = 5 mintutes
