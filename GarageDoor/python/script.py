import webiopi
import time
import os

GPIO = webiopi.GPIO

PIN_GARAGE = 17

def setup():
	GPIO.setFunction(PIN_GARAGE, GPIO.OUT)
	GPIO.digitalWrite(PIN_GARAGE, GPIO.HIGH)

#def loop():
	# Nothing for now.

def destroy():
	GPIO.digitalWrite(PIN_GARAGE, GPIO.HIGH)	

@webiopi.macro
def toggle_garage():
	GPIO.digitalWrite(PIN_GARAGE, GPIO.LOW)
	time.sleep(1)
	GPIO.digitalWrite(PIN_GARAGE, GPIO.HIGH)

@webiopi.macro
def restart_pi():
	os.system("sudo reboot")
