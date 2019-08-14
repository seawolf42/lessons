<!-- begin auto-generated title section -->
# Program 2: Touchpads
<!-- end auto-generated section -->


## Time Box

15 minutes


## Overview

In this exercise we will be using the touch sensors and the colored pixels around the edge of the board. When you touch one of the touch-enabled sensors, the respective pixel will light up, and when you remove your finger the pixel will turn black again.

**Note:** the pixels are numbered in a different pattern than the touch sensors, so the pixel that lights might be next to the touch sensor in some cases and somewhere else on the board for others.


## What to Do

Enter the following program in your editor:


```python
from adafruit_circuitplayground.express import cpx

import time

cpx.pixels.auto_write = False
cpx.pixels.brightness = 0.25

black = (0, 0, 0)
white = (255, 255, 255)

def get_color(switch, color=white):
    return color if switch else black

print('starting main loop')
while True:
    cpx.pixels[0] = get_color(cpx.touch_A1)
    cpx.pixels[1] = get_color(cpx.touch_A2)
    cpx.pixels[2] = get_color(cpx.touch_A3)
    cpx.pixels[3] = get_color(cpx.touch_A4)
    cpx.pixels[4] = get_color(cpx.touch_A5)
    cpx.pixels[5] = get_color(cpx.touch_A6)
    cpx.pixels[6] = get_color(cpx.touch_A7)
    cpx.pixels.show()
    time.sleep(.1)
```

Save the program on your CPX as `code.py`. Once it saves, you should be able to touch the capacitive touchpads (A1 through A7) and see the corresponding NeoPixel light up.

![green sticky note](images/sticky-note-green.png)


# Deep Dive

### NeoPixels

NeoPixels are multi-color LEDs. The board has 10 of them (though we only use 7 in this exercise). The NeoPixels are the little clear/white plastic items forming a ring about 1/2 way from the center of the board. They are just like pixels on a TV except they are bigger (obviously) and brighter.

You can access them by assigning a color value to each one using `cpx.pixels[index] = color`. Remember that in most cases computers start counting at 0, so the NeoPixels are `cpx.pixels[0]`, `cpx.pixels[1]`, ..., `cps.pixels[9]`.

You assign colors to them very similar to the way you indicate color for anything else in most computer languages: specifying a red, green, and blue brightness value for each pixel. If you set all three values to 0 (using `cpx.pixels[0] = (0, 0, 0)`) the pixel will not emit any light on any of those colors, and if you set all values to 255 (using `cpx.pixels[1] = (255, 255, 255)`) the pixel will emit the maximum brightness it can of all three colors, which gives the impression of white. Different combinations of values other than 0 and 255 are used to create (almost) every color the human eye can see.

Turning the NeoPixels on full brightness will consume **a lot** of power, and your USB cable may not be able to fully power the board if they are all fully on. Also, they will be uncomfortalbe to look at up close. It would be challenging to figure out how to scale all your values appropriately for different combinations of values, so the `cpx` library includes a way to scale the overall brightness in a single place, the `cpx.pixels.brightness` property. Set this property to `1.0` for full brightness, `0` for no brightness, or any value in between. Generally `cpx.pixels.brightness = .25` is adequate for indoor, up-close use.

Also, it is common to want to update all the pixels simultaneously when you are creating certain kinds of animations, but that requires an extra step to tell the board to switch all pixels from their previous values to their new values. Setting `cpx.pixels.auto_write = True` (the default if you don't set this at all) will cause pixels to update immediately when you change their value. If you want them to all change simultaneously, set `cpx.pixels.auto_write = False` and then when you are ready to update them all call `cpx.pixels.show()`.

### Capacitive Touch Sensors

The capacitive touch sensors respond to electical signals (so you can wire them up to other hardware), but they also sense the touch of skin. This allows you to simply use your finger to turn their input values on or off.

There are 7 touch sensors on the board: A1 through A7 (the others do not respond to touch). You access them by reading from `cpx.touch_A1` through `cpx.touch_A7`; each one will return `True` when being touched (or when a 3v signal is applied to the input) and `False` otherwise.

Since we want the color to be the same for every pixel, we have a function that takes an input and returns the right color based on whether the switch is on or off:

```python
def get_color(switch, color=white):
    return color if switch else black
```

By calling this, we get back either the color we specify (the funciton's `color` parameter) or black (`(0, 0, 0)`) based on whether the source is `True` or `False` (respectively).


## Resources

* [Docs » adafruit_circuitplayground.express](https://circuitpython.readthedocs.io/projects/circuitplayground/en/latest/api.html)
* [CircuitPython Cap Touch](https://learn.adafruit.com/circuitpython-essentials/circuitpython-cap-touch)
* [CircuitPython NeoPixel](https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel)
* []()


<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [Program 1: Buttons and Red LED](./exercise_buttons_and_leds.md) | [Exercises](./exercises.md) | [Program 3: NeoPixels](./exercise_neopixels.md) |
<!-- end auto-generated section -->
