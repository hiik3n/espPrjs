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


print("Hi")

flashLed2Times()






