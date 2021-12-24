import kasa
import asyncio


fanAuto = kasa.SmartPlug('192.168.0.76')
asyncio.run(fanAuto.update())
asyncio.run(fanAuto.turn_on())
print (fanAuto.alias)

fanAuto.turn_off()
