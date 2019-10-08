import RPi.GPIO as gpio
import time

class WindowController():
	def __init__(self):
		self.channel1 = 40
		self.channel2 = 38
		gpio.setmode(gpio.BOARD)
		gpio.setup(self.channel1, gpio.OUT, initial=gpio.LOW)
		gpio.setup(self.channel2, gpio.OUT, initial=gpio.LOW)
		gpio.setwarnings(False)

	def run_test(self):
		while True:
			self.set_forward()
			time.sleep(10)
			self.stop()
			time.sleep(10)
			self.set_backwards()
			time.sleep(10)
			self.stop()
			time.sleep(10)

	def set_forward(self):
		gpio.output(self.channel1, gpio.HIGH)
		gpio.output(self.channel2, gpio.LOW)


	def set_backwards(self):
		gpio.output(self.channel1, gpio.LOW)
		gpio.output(self.channel2, gpio.HIGH)

	def stop(self):
		gpio.output(self.channel1, gpio.LOW)
		gpio.output(self.channel2, gpio.LOW)