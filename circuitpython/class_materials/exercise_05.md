<!-- begin auto-generated title section -->
<!-- end auto-generated section -->


## Time Box


## Overview

glow eyes


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

while True:
    cpx.pixels.brightness = simpleio.map_range(cpx.light, ambient * .7, 320, 0, .3)
    time.sleep(0.1)
```

Save the program on your CPX as `code.py`. Once it saves, you should be able to use your board as a light sensor: it will start with 2 NeoPixels lit dimly, and if you move it into brighter or darker ambient light the NeoPixels will get brighter or darker (respectively).

![green sticky note](images/sticky-note-green.png)


# Deep Dive

#TODO


<!-- begin auto-generated nav-links section -->
<!-- end auto-generated section -->
