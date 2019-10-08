import RPi.GPIO as gpio
import time

import asyncio


class WindowController:
    def __init__(self):
        self.channel1 = 40
        self.channel2 = 38
        self.opening_time = 15
        self.test_time = 5

        gpio.setmode(gpio.BOARD)
        gpio.setwarnings(False)
        gpio.setup(self.channel1, gpio.OUT, initial=gpio.LOW)
        gpio.setup(self.channel2, gpio.OUT, initial=gpio.LOW)

    async def run_test(self):
        while True:
            self.set_forward()
            await self.wait(self.test_time)
            self.stop()
            await self.wait(self.test_time)
            self.set_backwards()
            await self.wait(self.test_time)
            self.stop()
            await self.wait(self.test_time)

    async def open_window(self):
        print("opening window")
        self.set_forward()
        await self.wait(self.opening_time)
        self.stop()
        print("stopped")

    async def close_window(self):
        print("closing window")
        self.set_backwards()
        await self.wait(self.opening_time)
        self.stop()
        print("stopped")

    def set_forward(self):
        print("set forward")
        gpio.output(self.channel1, gpio.HIGH)
        gpio.output(self.channel2, gpio.LOW)

    def set_backwards(self):
        print("set backward")
        gpio.output(self.channel1, gpio.LOW)
        gpio.output(self.channel2, gpio.HIGH)

    def stop(self):
        print("stop")
        gpio.output(self.channel1, gpio.LOW)
        gpio.output(self.channel2, gpio.LOW)

    async def wait(self, wait_time):
        time.sleep(wait_time)
