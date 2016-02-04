import webiopi
import os

GPIO = webiopi.GPIO

PIN_LIGHT = 17

PIN_RIGHT_FORWARD = 27
PIN_RIGHT_BACKWARD = 22

PIN_LEFT_FORWARD = 23
PIN_LEFT_BACKWARD = 24

def setup():
	GPIO.setFunction(PIN_LIGHT, GPIO.OUT)
	
	GPIO.setFunction(PIN_RIGHT_FORWARD, GPIO.OUT)
	GPIO.setFunction(PIN_RIGHT_BACKWARD, GPIO.OUT)
	
	GPIO.setFunction(PIN_LEFT_FORWARD, GPIO.OUT)
	GPIO.setFunction(PIN_LEFT_BACKWARD, GPIO.OUT)

#def loop():
	# Nothing for now.

def destroy():
	lightsOff()

@webiopi.macro
def top_left():
	stop()
	GPIO.digitalWrite(PIN_RIGHT_FORWARD, GPIO.HIGH)

@webiopi.macro
def top_middle():
	stop()
	GPIO.digitalWrite(PIN_RIGHT_FORWARD, GPIO.HIGH)
	GPIO.digitalWrite(PIN_LEFT_FORWARD, GPIO.HIGH)

@webiopi.macro
def top_right():
	stop()
	GPIO.digitalWrite(PIN_LEFT_FORWARD, GPIO.HIGH)

@webiopi.macro
def middle_left():
	stop()
	GPIO.digitalWrite(PIN_RIGHT_FORWARD, GPIO.HIGH)
	GPIO.digitalWrite(PIN_LEFT_BACKWARD, GPIO.HIGH)

@webiopi.macro
def middle_middle():
	stop()

@webiopi.macro
def middle_right():
	stop()
	GPIO.digitalWrite(PIN_RIGHT_BACKWARD, GPIO.HIGH)
	GPIO.digitalWrite(PIN_LEFT_FORWARD, GPIO.HIGH)

@webiopi.macro
def bottom_left():
	stop()
	GPIO.digitalWrite(PIN_RIGHT_BACKWARD, GPIO.HIGH)

@webiopi.macro
def bottom_middle():
	stop()
	GPIO.digitalWrite(PIN_RIGHT_BACKWARD, GPIO.HIGH)
	GPIO.digitalWrite(PIN_LEFT_BACKWARD, GPIO.HIGH)

@webiopi.macro
def bottom_right():
	stop()
	GPIO.digitalWrite(PIN_LEFT_BACKWARD, GPIO.HIGH)

@webiopi.macro
def stop():
	GPIO.digitalWrite(PIN_RIGHT_FORWARD, GPIO.LOW)
	GPIO.digitalWrite(PIN_RIGHT_BACKWARD, GPIO.LOW)
	GPIO.digitalWrite(PIN_LEFT_FORWARD, GPIO.LOW)
	GPIO.digitalWrite(PIN_LEFT_BACKWARD, GPIO.LOW)

@webiopi.macro
def lightsOn():
	GPIO.digitalWrite(PIN_LIGHT, GPIO.HIGH)

@webiopi.macro
def lightsOff():
	GPIO.digitalWrite(PIN_LIGHT, GPIO.LOW)

@webiopi.macro
def getLights():
	if (GPIO.digitalRead(PIN_LIGHT) == GPIO.LOW):
		return false
	return true

@webiopi.macro
def restart_pi():
	os.system("sudo reboot")
