import time
import pytz
from datetime import datetime
#dhtDevice = adafruit_dht.DHT22(board.D7)


while True:
    now = datetime.now(tz=pytz.utc)
    denverNow = now.astimezone(pytz.timezone('US/Mountain'))
    minutes = int(denverNow.strftime('%S'))
    print (minutes)
    time.sleep(1) 
    if minutes % 5 == 0:
        print (str(minutes) +' code ran!')
