import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

led = 5 # GPIO pin number is 5 and name is GPIO3

GPIO.setup(led, GPIO.OUT, initial = 0) # Setup LED and set it initially to OFF

def on():
        GPIO.output(led, GPIO.HIGH) # Set LED to ON

def off():
        GPIO.output(led, GPIO.LOW) # Set LED to OFF