<!-- begin auto-generated title section -->
# Installing/Updating CircuitPython
<!-- end auto-generated section -->


## Time Box

15 minutes


## Overview

The first task with your new board is to install [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython) on it (it comes with [MicroPython](https://micropython.org/) out of the box).


## What to Do

1. [Download CircuitPython for the Circuit Playground Express](https://circuitpython.org/board/circuitplayground_express/) and save it locally to wherever you usually save downloads.
    * <img src="./images/icon-windows.jpg" height ="25" align="left" alt="windows logo">&nbsp;**Note:** If you are using Windows 7 there are also drivers you will need to install, see [the section about this](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython#windows-7-drivers-5-13) in the official installation guide.
1. Plug your CPX board into your computer (make sure you can see it as a mounted drive)
1. Find the reset button on your board... it's right in the middle
1. Press the reset button twice in a row
1. Your computer should now show a drive called `CPLAYBOOT`
1. Drag the file you downloaded onto the `CPLAYBOOT` drive
1. Watch as a couple lights flash and the board re-mounts as `CIRCUITPY`
1. [Download the Adafruit_CircuitPython_Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases) and save it locally to wherever you usually save downloads
    * Pick the correct one by matching the release number in the filename (like `4.x`) to the release number of Circuit Python that you downloaded above
1. Unzip the bundle
1. Copy the `simpleio.mpy` file in the `lib` folder to the `lib` folder of your CPX board

![green sticky note](images/sticky-note-green.png)


## Discussion

The board comes with `micropython` installed, which requires all kinds of tools and extra learning to really get up and running. You're here because you want to use `circuitpython`!

One nice thing about the AdaFruit boards is that they are designed to make this upgrade easy. Any time you want to reset your board or want the latest version of `circuitpython`, just follow the steps above.

The bundle that you downloaded contains all the extra libraries beyond the standard library that AdaFruit maintains for advanced functionality. In this workshop we only actually need `simpleio`.


## References

* [Installing CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)
* [Download CircuitPython for Circuit Playground Express](https://circuitpython.org/board/circuitplayground_express/)
* [Adafruit_CircuitPython_Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle)


<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [Setting Everything Up](./setup.md) | [Setting Everything Up](./setup.md) | [Connecting to Your Computer](./setup_connection.md) |
<!-- end auto-generated section -->
