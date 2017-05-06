#	pyEsp8266ReadLm35Print2x7Led
import time as t
from machine import Pin
import network
import urequests


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

def list_available_wlans():
	nic = network.WLAN(network.STA_IF)
	if not nic.active():
		nic.active(True)
	_res = nic.scan()
	for _wlan in _res:
		print([str(_i) for _i in _wlan])
	return [[_i[0] for _i in _res], _res]

list_available_wlans()[0]

url = 'https://www.amdoren.com/api/timezone.php?api_key=%s&loc=Ho+Chi+Minh+City' % ''
response = urequests.get(url)
resJson = response.json()
response.close()

print("Hi")

flashLed2Times()
howTemp()






