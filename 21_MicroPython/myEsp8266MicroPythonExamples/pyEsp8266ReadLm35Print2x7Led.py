#	pyEsp8266ReadLm35Print2x7Led
import time as t
from machine import Pin


def flashLed2Times():
	p2 = Pin(2, Pin.OUT)
	p2.high()
	t.sleep(2)
	p2.low()
	t.sleep(2)
	p2.high()
	t.sleep(2)
	p2.low()
	t.sleep(2)
	p2.high()

def setPinHigh(pinNo):
	_pin = Pin(pinNo, Pin.OUT)
	_pin.high()

def setPinLow(pinNo):
	_pin = Pin(pinNo, Pin.OUT)
	_pin.low()

def readAdc0():
	from machine import ADC
	return ADC(0).read()

def howTemp():
	return readAdc0()*3/1023*100

def set7Led(num, portLists=[], isAnodeCommon=True):
	# 	  6
	#    ---
	# 5 | 4 | 7
	#    ---
	# 1 |   | 3
	#    ---	. 8
	#     2

	ledLib = {
		0 : [1,2,3,5,6,7],
		1 : [3,7],
		2 : [1,2,4,6,7],
		3 : [2,3,4,6,7],
		4 : [3,4,5,7],
		5 : [2,3,4,5,6],
		6 : [1,2,3,4,5,6],
		7 : [3,6,7],
		8 : [1,2,3,4,5,6,7],
		9 : [2,3,4,5,6,7]
	}

	if len(portLists) != 8:
		return

	for _i in ledLib.get(num, []):
		_index = _i - 1
		if isAnodeCommon:
			setPinLow(portLists[_index])
		else:
			setPinHigh(portLists[_index])

def readTempFlashLed(portLed, timeDur=2):
	setPinHigh(portLed)
	t.sleep(timeDur)
	setPinLow(portLed)
	return howTemp()


print("Hi")

flashLed2Times()
howTemp()






