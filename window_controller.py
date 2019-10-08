import RPi.GPIO as gpio
import time

channel = 40

gpio.setmode(gpio.BOARD)
gpio.setup(channel, gpio.OUT)

while True:
	gpio.output(channel, gpio.HIGH)