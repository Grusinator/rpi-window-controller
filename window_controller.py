import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

#while True:
gpio.output(18, gpio.HIGH)