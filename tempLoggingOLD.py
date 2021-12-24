# !/usr/bin/python3


import gspread
import random
import time
import Adafruit_DHT
import pytz
from datetime import datetime

''' To run this file indefinately run
    nohop python openSheet.py
'''
# google sheets authentication and loading worksheet in file.
gs = gspread.service_account()
sh = gs.open("TemperatureLogging")
worksheet = sh.sheet1
# gets value form a single cell
# for now the place where the last updated cell is in "C2"
lastUpdatedCell = 0
timeStamp = 0
while True:
    # getting now
    now = datetime.now(tz=pytz.utc)
    denverNow = now.astimezone(pytz.timezone('US/Mountain'))

    # getting temperature reading
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    humidity = '%.2f' % (humidity)
    temperature = '%.2f' % (temperature)

    # get last updated value
    lucplace = 'D2'
    lastUpdatedCell = worksheet.acell(lucplace).value
    lastUpdatedCell = int(lastUpdatedCell) + 1
    lastUpdatedCell = str(lastUpdatedCell)

    '''update cells'''
    worksheet.update('A' + lastUpdatedCell, str(denverNow.date()))  # u$
    worksheet.update('B' + lastUpdatedCell,
                     str(denverNow.strftime('%H:%M')))  # u$
    worksheet.update('C' + lastUpdatedCell, str(temperature))  # u$
    # print what has been done
    print('added' + str(denverNow.date()) + ' and ' + str(temperature))

    # update last updated cell
    worksheet.update(lucplace, lastUpdatedCell)

    # sleeping
    time.sleep(300)
