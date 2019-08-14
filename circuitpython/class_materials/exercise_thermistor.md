<!-- begin auto-generated title section -->
# Program 4: Thermister
<!-- end auto-generated section -->


## Time Box

15 minutes


## Overview

The board has a thermal sensor that can be used to make a simple thermometer. We will first calibrate to the current temperature, then show more or fewer red lights as the temperature around the device changes.


## What to Do

Enter the following program in your editor:

```python
from adafruit_circuitplayground.express import cpx
import time
import simpleio

cpx.pixels.auto_write = False
cpx.pixels.brightness = 0.25

black = (0, 0, 0)
color = (255, 0, 0)

ambient = cpx.temperature
print('ambient:', ambient)

print('starting main loop')
while True:
    temperature = cpx.temperature
    print('temperature:', cpx.temperature)
    measurement = simpleio.map_range(
        temperature,
        ambient - .5,
        ambient + 2.5,
        0,
        10,
    )
    print('measurement:', measurement)
    for i in range(10):
        cpx.pixels[i] = color if i < measurement else black
    cpx.pixels.show()
    time.sleep(.1)
```

Save the program on your CPX as `code.py`. Once it saves, you should be able to use your board as a thermometer: it will start with two NeoPixels lit, and if you touch the thermal sensor additional lights should light to show the increase in temperature from your skin.

![green sticky note](images/sticky-note-green.png)


## Deep Dive

There are a few new things going on in this program, so let's break them down.


### Thermistor (Thermal Sensor)

The CPX board has a thermistor that returns the temperature in degrees celsius. You read the value at `cpx.temperature` and you get back a floating point value.


### Ambient Temperature

When this program is first run, it might be at the beach or in a snowstorm. Showing changes in temperature across such a wide range of possible values make it hard to see small changes. Instead we calibrate the sensor first and then show changes near that calibrated value.

The basic strategy for this is to measure the temperature when the program starts and just save it. That becomes the benchmark for all future readings to be compared to. That initial reading will be represented by "two point five" lights, so we can see two lights light up initially and then compare future readings to that value do display an appropriate new number of lights.


### Range-Scaling Values

Once we have the ambient temperature, we continuously re-read the temperature in a loop, decide how many lights to light, and display them. Since doing math to scale numbers to different vector spaces is hard to get right, we will use the `simpleio` package's `map_range()` function.

```python
import simpleio

threshold = simpleio.map_range(
    cpx.temperature,
    ambient - .5,
    ambient + 2.5,
    0,
    10,
)
```

The `map_range()` function takes 5 values:

* the value to map from one scale to the other
* the lower bound for the original scale (the scale the value is on)
* the upper bound for the original scale
* the lower bound for the target scale
* the upper bound for the target scale

In the call above, we are effectively saying, "take the value we just read, and put it on a scale from 1/2 degree below to 2.5 degrees above the ambient temperature (whatever it was) and map it to a value from 0 to 10". As long as the current temperature is within that range, some number of lights will be lit. If it goes below or above that range, all or none (respectively) of the lights will be lit.

We then use that value to set the appropriate color to each of the NeoPixels.


### Print Statements

Don't forget to use `print()` statements liberally to see what's going on in your code!


## References

* [Docs » adafruit_circuitplayground.express](https://circuitpython.readthedocs.io/projects/circuitplayground/en/latest/api.html)
* []()


<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [Program 3: NeoPixels](./exercise_neopixels.md) | [Exercises](./exercises.md) | [Program 5: Light Sensor](./exercise_phototransistor.md) |
<!-- end auto-generated section -->
