import RPi.GPIO as gpio
import time


class WindowController():
	def __init__(self):
		channel1 = 40
		channel2 = 38
		gpio.setmode(gpio.BOARD)
		gpio.setup(channel1, gpio.OUT, gpio.LOW)
		gpio.setup(channel2, gpio.OUT, gpio.LOW)

	def run_test(self)
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
		gpio.output(channel1, gpio.HIGH)
		gpio.output(channel2, gpio.LOW)


	def set_backwards(self):
		gpio.output(channel1, gpio.LOW)
		gpio.output(channel2, gpio.HIGH)

	def stop(self):
		gpio.output(channel1, gpio.LOW)
		gpio.output(channel2, gpio.LOW)

if __name__ == "__main__":
	controller = WindowController()
	controller.run_test()