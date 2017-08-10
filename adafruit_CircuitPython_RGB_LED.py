# The MIT License (MIT)
#
# Copyright (c) 2017 Asher Lieber for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_CircuitPython_RGB_LED`
====================================================

TODO(description)

* Author(s): Asher Lieber
"""

import digitalio
import pulseio
import board
import time

class rgb_led(object):
    def __init__(self, pin_r, pin_g, pin_b):
        self.red_led   = pulseio.PWMOut(pin_r)
        self.green_led = pulseio.PWMOut(pin_g)
        self.blue_led  = pulseio.PWMOut(pin_b)

    def set_color(self, r, g, b):
           self.red_led.duty_cycle = (65535-int(self.map_range(r, 0, 255, 0, 65535)))
           self.green_led.duty_cycle = (65535-int(self.map_range(g, 0, 255, 0, 65535)))
           self.blue_led.duty_cycle = (65535-int(self.map_range(b, 0, 255, 0, 65535)))

    def map_range(self, x, in_min, in_max, out_min, out_max):
        return max(min((x-in_min) * (out_max - out_min) / (in_max-in_min) + out_min, out_max), out_min)
