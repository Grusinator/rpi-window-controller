import time

import RPi.GPIO as gpio


class WindowController:
    def __init__(self):
        self.channel1 = 40
        self.channel2 = 38
        self.opening_time = 10
        self.test_time = 5
        self.STOP = False
        
        gpio.setmode(gpio.BOARD)
        gpio.setwarnings(False)
        gpio.setup(self.channel1, gpio.OUT, initial=gpio.LOW)
        gpio.setup(self.channel2, gpio.OUT, initial=gpio.LOW)
        self.close_window()
        self.state_open_level = 0.0

    def timed_ventilation(self, mins: float):
        self.open_window()
        self.wait(mins * 60)
        self.close_window()

    def run_test(self):
        while True:
            if self.STOP is True:
                self.STOP = False
                break
            self.set_forward()
            self.wait(self.test_time)
            self.stop()
            self.wait(self.test_time)
            self.set_backwards()
            self.wait(self.test_time)
            self.stop()
            self.wait(self.test_time)

    def open_window(self):
        print("opening window")
        self.set_forward()
        self.wait(self.opening_time)
        self.state_open_level = 1
        self.stop()
        print("stopped")

    def close_window(self):
        print("closing window")
        self.set_backwards()
        self.wait(self.opening_time)
        self.state_open_level = 2
        self.stop()
        print("stopped")

    def set_forward(self):
        print("set forward")
        gpio.output(self.channel1, gpio.LOW)
        gpio.output(self.channel2, gpio.HIGH)

    def set_backwards(self):
        print("set backward")
        gpio.output(self.channel1, gpio.HIGH)
        gpio.output(self.channel2, gpio.LOW)

    def stop(self):
        print("stop")
        gpio.output(self.channel1, gpio.LOW)
        gpio.output(self.channel2, gpio.LOW)

    def wait(self, wait_time):
        time.sleep(wait_time)
