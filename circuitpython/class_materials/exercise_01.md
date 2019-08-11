<!-- begin auto-generated title section -->
<!-- end auto-generated section -->


## Time Box

15 minutes


## Overview

Now that we have connected the board and successfully tested it, it's time to make it do something. The best starting point is blinking a light on the board, but we already made one of those when we first tested the connection. Let's make the light respond to our interactions with the board!

The goal is to have the switch control which button is controlling the LED, and to turn on the LED when that button is pressed and turn it off when the button is released.

| Switch | Button A | Button B | LED |
|---|---|---|---|
| **Left** | **Off** | Off | **Off** |
| **Left** | **On** ✅ | Off | **On** ✅ |
| **Left** | **Off** | On | **Off** |
| **Left** | **On** ✅ | On | **On** ✅ |
| **Right** | Off | **Off** | **Off** |
| **Right** | On | **Off** | **Off** |
| **Right** | Off | **On** ✅ | **On** ✅ |
| **Right** | On | **On** ✅ | **On** ✅ |

Notice how the LED state is controlled by either button A or button B based on the switch selection (the bold text in the table should help you see the pattern).


## What to Do

Enter the following program in your editor:

```python
from adafruit_circuitplayground.express import cpx

import time

print('starting main loop')
while True:
    if cpx.switch:
        cpx.red_led = cpx.button_a
    else:
        cpx.red_led = cpx.button_b
    time.sleep(.1)
```

Save the program on your CPX as `code.py`. Once it saves, you should be able to push buttons and play with the switch and see the LED responding as expected.

![green sticky note](images/sticky-note-green.png)


## Deep Dive

To interact with any of the board's hardware, we need to import the library that controls this. That library is called `adafruit_circuitplayground.express`, and it has an object called `cpx`. We get this into our program by importing in the following way:

```python
from adafruit_circuitplayground.express import cpx
```

Because this import is required for just about any program you will write for your CPX, we follow the convention of always making it the top line of every program.


### Printing

Since there's not really a way to debug a program on the board itself, the easiest way to debug is to print output to the console. Use `print()` statements wherever you want to find out what's going on in your program!


### Red LED

There is one red LED on the board, and it can be controlled by setting the `cpx.red_led` property to `True` (on) or `False` (off).


### Buttons

There are two buttons on the board that are `True` when pressed and `False` when not pressed. Their values can be read at `cpx.button_a` and `cpx.button_b`.


### Switch

There is a two-position switch on the board that is `True` when it is moved to the left and `False` when it it moved to the right. It can be read at `cpx.switch`.


### Program Loop (Event Loop)

Since we continually need to re-test the position of all the controls, the program should be run in a loop. I recommend putting a slight delay before repeating the loop each time to minimize power consumption on the board. This is most easily handled with the following pattern:

```python
import time
# ... possibly other imports

while True:
    # ... do some stuff
    time.sleep(.1)  # sleep for 100 ms
```

Sleep times are entered as seconds and can either be integer or floating-point values. `time.sleep(.1)` will cause the board to do nothing at all for 100ms (0.1 seconds). Typically the longer the board sleeps between iterations of the loop, the less power it uses but the more "laggy" it seems from when you push a button until you see the result. I have found that right around 100ms is where the response is fast enough that it's not distracting, but you might want a smaller value if responsiveness is not quick enough for your liking (try `.05` to see the difference).


## References

* [Docs » adafruit_circuitplayground.express](https://circuitpython.readthedocs.io/projects/circuitplayground/en/latest/api.html)
* []()


<!-- begin auto-generated nav-links section -->
<!-- end auto-generated section -->
