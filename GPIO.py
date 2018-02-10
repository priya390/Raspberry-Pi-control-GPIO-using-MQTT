import time
import RPi.GPIO as GPIO
import Adafruit_DHT

GPIO.setmode(GPIO.BOARD)

led = 5 # GPIO pin number is 5 and name is GPIO3
DHT = 27 # GPIO27 for DHT11 sensor

GPIO.setup(led, GPIO.OUT, initial = 0) # Setup LED and set it initially to OFF

def on():
        GPIO.output(led, GPIO.HIGH) # Set LED to ON

def off():
        GPIO.output(led, GPIO.LOW) # Set LED to OFF

def temp():
        temperature = Adafruit_DHT.read_retry(11, DHT)[1]
        return temperature

def hum():
        humidity = Adafruit_DHT.read_retry(11, DHT)[0]
        return humidity