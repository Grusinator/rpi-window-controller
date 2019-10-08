import RPi.GPIO as gpio
import time

channel1 = 40
channel2 = 38

gpio.setmode(gpio.BOARD)
gpio.setup(channel1, gpio.OUT)
gpio.setup(channel2, gpio.OUT)

while True:
	set_forward()
	time.sleep(4)
	set_backwards()
	time.sleep(4)


def set_forward():
	gpio.output(channel1, gpio.HIGH)
	gpio.output(channel2, gpio.LOW)


def set_backwards():
	gpio.output(channel1, gpio.LOW)
	gpio.output(channel2, gpio.HIGH)

