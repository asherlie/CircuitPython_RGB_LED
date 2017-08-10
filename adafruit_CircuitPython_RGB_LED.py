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
import random

class rgb_led(object):
    """
    allows for easy control of RGB LEDs

    :param ~pulseio.PWMOut pin_r: PWM pin connected to red wire of RGB LED
    :param ~pulseio.PWMOut pin_g: PWM pin connected to green wire of RGB LED
    :param ~pulseio.PWMOut pin_b: PWM pin connected to blue wire of RGB LED

    Example for Metro M0 Express:
        .. code-block:: python
            
            import adafruit_CircuitPython_RGB_LED as rgb_led
            import board

            # red wire attached to D8, green to D9, blue to D10
            led = rgb_led.rgb_led(board.D8, board.D9, board.D10)
            # set color to purple!
            led.set_color(255, 0, 255)
    """

    def __init__(self, pin_r, pin_g, pin_b):
        self.red_led   = pulseio.PWMOut(pin_r, duty_cycle=65535)
        self.green_led = pulseio.PWMOut(pin_g, duty_cycle=65535)
        self.blue_led  = pulseio.PWMOut(pin_b, duty_cycle=65535)

    def set_color(self, r, g, b):
        """sets RGB LED to a coloor based on RGB values
        :param int r: red value ouf of 255
        :param int g: green value ouf of 255
        :param int b: blue value ouf of 255
        """
        self.red_led.duty_cycle = (65535-int(self.map_range(r, 0, 255, 0, 65535)))
        self.green_led.duty_cycle = (65535-int(self.map_range(g, 0, 255, 0, 65535)))
        self.blue_led.duty_cycle = (65535-int(self.map_range(b, 0, 255, 0, 65535)))

    def map_range(self, x, in_min, in_max, out_min, out_max):
        """
        Maps a number from one range to another.
        Note: This implementation handles values < in_min differently than arduino's map function does.
        :return: Returns value mapped to new range
        :rtype: float
        """
        return max(min((x-in_min) * (out_max - out_min) / (in_max-in_min) + out_min, out_max), out_min)
