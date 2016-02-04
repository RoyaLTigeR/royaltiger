import webiopi
import time
import os

GPIO = webiopi.GPIO

PIN_GATE = 17

def setup():
	GPIO.setFunction(PIN_GATE, GPIO.OUT)
	GPIO.digitalWrite(PIN_GATE, GPIO.HIGH)

#def loop():
	# Nothing for now.

def destroy():
	GPIO.digitalWrite(PIN_GATE, GPIO.HIGH)	

@webiopi.macro
def toggle_gate():
	GPIO.digitalWrite(PIN_GATE, GPIO.LOW)
	time.sleep(1)
	GPIO.digitalWrite(PIN_GATE, GPIO.HIGH)

@webiopi.macro
def restart_pi():
	os.system("sudo reboot")
