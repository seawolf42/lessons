<!-- begin auto-generated title section -->
# Program 5: Light Sensor
<!-- end auto-generated section -->


## Time Box

10 minutes


## Overview

The board has a light sensor that can be used to measure the brightness around the board. We will first calibrate to the current brightness, then show brighter or darker pixels as the light around the device changes.


## What to Do

Enter the following program in your editor:

```python
from adafruit_circuitplayground.express import cpx

import time
import simpleio

cpx.pixels.brightness = 0.3

color = (255, 255, 255)

cpx.pixels[0] = color
cpx.pixels[9] = color

ambient = cpx.light
print('ambient:', ambient)

print('starting main loop')
while True:
    cpx.pixels.brightness = simpleio.map_range(cpx.light, ambient * .3, 320, 0, .3)
    time.sleep(0.1)
```

Save the program on your CPX as `code.py`. Once it saves, you should be able to use your board as a light sensor: it will start with 2 NeoPixels lit dimly, and if you move it into brighter or darker ambient light the NeoPixels will get brighter or darker (respectively).

![green sticky note](images/sticky-note-green.png)


## Deep Dive

This program is similar to the last in that it starts by taking an ambient measurement (of light this time instead of temperature) and then indicating changes to that ambient value, but this time we use brightness to indicate change rather than number of lights.

We start by turning on pixels 0 and 9 (at the top of the board) to white. The CPX board has a light sensor that returns the brightness. You read the value at `cpx.light` and you get back a floating point value. We read the ambient light and then repeatedly compare current to ambient and translate our number on that scale to a brightness value between 0 and .3.


## Experience Points

See if you can modify this program so that the ambient level adjusts slowly towards the current reading. This will cause the lights to brighten when the board goes from dark to light but then dim again as they re-normalize for the new light level.


## Resources

* [Docs » adafruit_circuitplayground.express](https://circuitpython.readthedocs.io/projects/circuitplayground/en/latest/api.html)
* []()


<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [Program 4: Thermister](./exercise_thermistor.md) | [Exercises](./exercises.md) | [Program 6: Accelerometer](./exercise_accelerometer.md) |
<!-- end auto-generated section -->
