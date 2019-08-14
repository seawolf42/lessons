<!-- begin auto-generated title section -->
# Program 6: Accelerometer
<!-- end auto-generated section -->


## Time Box

15 minutes


## Overview

The board has an accelerometer that can be used to measure the acceleration being applied to the board in three dimensions. By combining these measurements, you can figure out which way is "up" (if the board is stationary) or which way the board is being accelerated (if it is in motion).


## What to Do

Enter the following program in your editor:

```python
from adafruit_circuitplayground.express import cpx

import math
import simpleio
import time

cpx.pixels.brightness = 0.3

color = (255, 255, 255)
black = (0, 0, 0)

print('starting main loop')
while True:
    x, y, z = cpx.acceleration
    r = math.atan2(x, y)
    pixel = round(simpleio.map_range(r, -math.pi, math.pi, 5, -5) - .5) % 10
    print('({0:+0.3f}, {1:+0.3f}, {2:+0.3f}) -> {3}'.format(x, y, z, pixel))
    for i in range(10):
        cpx.pixels[i] = color if i == pixel else black
    cpx.pixels.show()
    time.sleep(0.1)
```

Save the program on your CPX as `code.py`. Once it saves, you should be able to use your board as a level: it will light the NeoPixel that is highest on the board (measured from level ground).

![green sticky note](images/sticky-note-green.png)


## Deep Dive

There's a lot going on in this program, let's dive in!

### Accelerometer

The board has an accelerometer that returns a tuple of three values:

```python
x, y, z = cpx.accelerometer
```

Each value is the acceleration in ft/s (feet per second) measured on that axis.

The x-axis bisects the board from the USB connector to the power plug, so if the right side of the board (the `GND` connector between `A1` and `A2`) is straight up `x` will be ~9.8, and if the `3.3V` connector directly opposite is straight up `x` will be ~-9.8.

The y-axis bisects the board between those two pins, so if the USB connector is straight up `y` will be ~9.8, and if the power plug is straight up `y` will be ~-9.8.

The z-axis is perpendicular to the plane of the board, so if the board is sitting flat right-side up `z` will be ~9.8, and if it is inverted `z` will be ~-9.8.

Of course, if the board is being accelerated by anything other than gravity (its motion vector is changing on any axis) then the numbers can be higher or lower.


### Converting X and Y to a Direction

I bet you thought you would never see `arctangent` again in your life, right? Wrong! We're using it today.

An arctangent finds a rotational value given a ratio between the rise and the run of the vector being measured. We're using `math.atan2` which takes 2 values (`x` and `y`) and determines the rotation.

![wait, wut?](./images/wut1.png)

What that basically means is given an X and Y, `math.atan2(x, y)` gives us back a number from `-π` to `+π` telling us the angle between the ray defined by `x` and `y` and the reference vector (the positive x-axis).

![wait, wut?](./images/wut2.png)

Ok, basically if we call `math.atan2(x, y)`, we get back a number from `-π` to `+π`.


### Adjusting the Reference

The second thing we have going on here is that we have to take that value and map it to a single light, with values ranging from 0 to 9. This looks like a job for `map_range()`!

First we map the raw value to the right range scale (almost):

```python
pixel_id = simpleio.map_range(r, -math.pi, math.pi, 5, -5)
```

... then we add a little bit to account for the offset of the pixels themselves, because `pixel[0]` is not straight up but rather about 1/20 of a rotation clockwise from straight up, so add `0.5` to the value above:

```python
pixel_id = simpleio.map_range(r, -math.pi, math.pi, 5, -5) + 0.5
```

... then we round to an integer value:

```python
pixel_id = round(simpleio.map_range(r, -math.pi, math.pi, 5, -5) + 0.5)
```

... and finally we take our number in the range (-5, 4) and convert it to (0, 10) using modulus:

```python
pixel_id = round(simpleio.map_range(r, -math.pi, math.pi, 5, -5) + 0.5) % 10
```

The net result is that for any combination of `x` and `y`, we get back the ID of the pixel that is closest to "up" for those values.

## Experience Points

See if you can modify this program so that the brightness of the pixel changes as the board is more or less flat, so that if the pixel is straight up it is very bright and if it is close to level the pixel is less bright.


## Resources

* [Docs » adafruit_circuitplayground.express](https://circuitpython.readthedocs.io/projects/circuitplayground/en/latest/api.html)
* [Acceleration](https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/acceleration)
* [2-Argument Arctangent](https://en.wikipedia.org/wiki/Atan2)
* [`math.atan2(x, y)`](https://docs.python.org/3/library/math.html#math.atan2)


<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [Program 5: Light Sensor](./exercise_phototransistor.md) | [Exercises](./exercises.md) | [Final Remarks](./final.md) |
<!-- end auto-generated section -->
