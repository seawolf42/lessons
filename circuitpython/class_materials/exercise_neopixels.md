<!-- begin auto-generated title section -->
# Program 3: NeoPixels
<!-- end auto-generated section -->


## Time Box

15 minutes


## Overview

This exersize shows how to create a simple animation using the NeoPixels.

In the last exercise we light them individually, but we can also light them in unison or separately and perform some clever animations.


## What to Do

Enter the following program in your editor:

```python
from adafruit_circuitplayground.express import cpx

cpx.pixels.auto_write = False
cpx.pixels.brightness = 0.25

black = (0, 0, 0)
color = (255, 0, 0)
decay = 26

def decay_color(current):
    return [max(c - decay, 0) for c in current]

current = 0

print('starting main loop')
while True:
    cpx.pixels[current] = color
    cpx.pixels.show()
    for i in range(10):
        cpx.pixels[i] = decay_color(cpx.pixels[i])
    cpx.pixels.show()
    current += 1
    current %= 10
```

Save the program on your CPX as `code.py`. Once it saves, you should see the NeoPixels animate a circular "ring of fire" around the board.

![green sticky note](images/sticky-note-green.png)


# Deep Dive

This program demonstrates a very simple animation loop. The loop picks a `current` pixel (starting at `0`) and lights it, then it reduces the color of each pixel by a set amount, then it advances to the next pixel and repeats the process. The net effect is any one pixel gets bright and then slowly dims, and the animation appears to be a rotating ring of light around the board.

The `decay_color()` method is similar to the `get_color()` method from the last example in that it retuns a color tuple every time it's called. It differs, however, in that it takes a color as a parameter and returns a color that is not as bright as the color passed in. It dims each of the RGB values by the same amount, so under some circumstances it will actually change the color. To see what happens, change the `color = (255, 0, 0)` line to `color = (255, 150, 75)`. To properly dim without changing color, it would have to multiply each component by the same reduction factor instead of doing simple subtraction.

The main loop first sets the `current` pixel to the primary `color`, then calls `decay_color()` for each pixel on the board and causes all of them to display. Finally it updates the value of `current` by incrementing it (`color += 1`) and rolling it back to the start once it has passed the last pixel (`color %= 10`).

## References

* [Docs » adafruit_circuitplayground.express](https://circuitpython.readthedocs.io/projects/circuitplayground/en/latest/api.html)
* [CircuitPython NeoPixel](https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel)


<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [Program 2: Touchpads](./exercise_touchpads.md) | [Exercises](./exercises.md) | [Program 4: Thermometer](./exercise_thermometer.md) |
<!-- end auto-generated section -->
