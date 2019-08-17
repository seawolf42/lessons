<!-- begin auto-generated title section -->
# Connecting to Your Computer
<!-- end auto-generated section -->


## Time Box

15 minutes


## Overview

It's common to write a "hello world" program as your first experiment in any language. We don't have a screen, though, so we can't really do that. So how do we see what the board has to say?

Simple, we set up a serial connection to the board. The board is connected through a USB cable, and USB is just a particular kind of serial connection. What we want to do is see the output of a print statement on our computer screen.


## What to Do

Disconnect your board from your computer if it is connected. We will need to determine what `tty` device it is using.

**Note:** if you don't know what a `tty` device is, don't fret, the description below will go into a little more depth and there are a lot of pages online describing them. For now, just trust that the following will work.

The following steps will depend on whether you're using MacOS, Windows, or Linux (don't worry, this is the only place in the whole workshop where the instructions are different for different operating systems):

**Note:** many of these instructions include key combinations using the following notation convention:

* `^x`: hold down the control key and press `x`
* `CMD-x` (MacOS only): hold down the Command key (on either side of the spacebar) and press `x`
* `ALT-x` (Windows only): hold down the Alt key (on either side of the spacebar) and press `x`


### MacOS

<img src="./images/icon-mac.png" height="50" alt="macos logo">

1. In Finder, open `/Volumes/CIRCUITPY`
1. Open the Terminal app (press `CMD-spacebar` and type `terminal`)
1. Type `ls /dev/tty.*`
1. Connect your board to your computer
1. Type `ls /dev/tty.*` again
1. There should be one more item in the list this time than there was last time, figure out what the new one is and copy it to the clipboard
1. Type `screen /dev/<device> 115200` (replace `<device>` with the name of the copied device, something like `tty.usbmodem12345`)

**Note:** once you start the `screen` command, stopping it is not intuitive; to exit, press `^a` and then `^d`.

See [Advanced Serial Console on Mac and Linux](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-mac-and-linux) for more details if you're having trouble with this.


### Windows

<img src="./images/icon-windows.jpg" height ="50" alt="windows logo">

**Note:** this section assumes you have [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) installed; you will need this for communicating with your device

1. In Windows Explorer, open the USB drive for the device
1. Open Device Manager (press `ALT-spacebar` and type `device manager`)
1. Expand the "Ports" section and look at the list for `COMx` names, where `x` is a number (typically 1-4, so ultimately looking like `COM3`)
1. Connect your board to your computer
1. Examine the list under "Ports" again
1. There should be one more item in the list this time then there was before, figure out what the new one is and remember the number
1. Open Putty (press `ALT-spacebar` and type `putty`)
1. Under *connection type*, click *serial*
1. Under *serial line*, enter the `COMx` port you identified above
1. Under *speed*, enter `115200`
1. Click *open*

See [Advanced Serial Console on Windows](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-windows) for more details if you're having trouble with this.


### Linux

<img src="./images/icon-linux.jpg" height ="50" alt="linux logo">

1. On the desktop, open the list of external drives (will vary based on which Linux you use) and then open the CIRCUITPY drive
1. Open your command-line application (a `bash`/`zsh`/whatever-`sh` prompt)
1. Install `screen` if it isn't already installed
    1. `apt-get install screen` (possibly with `sudo`)
1. The rest of the instructions are exactly the same as for MacOS above starting with step 3 with the following exceptions:
    1. Instead of `ls /dev/tty.*` use `ls /dev/ttyACM*`
    1. You might need `sudo` to run the `screen` command in linux: `sudo screen /dev/<device> 115200`

**Note:** once you start the `screen` command, stopping it is not intuitive; to exit, press `^a` and then `^d`.

See [Advanced Serial Console on Mac and Linux](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-mac-and-linux) for more details if you're having trouble with this.


### Everyone

Put up your red sticky note if you have issues and need help. If you have no issues, keep going...

Once you've completed the above steps, connect your board to your computer, then enter the following program in your editor:

```python
from adafruit_circuitplayground.express import cpx
import time

while True:
    print('hello world!')
    cpx.red_led = not cpx.red_led
    time.sleep(.5)
```

Save the program on your CPX as `code.py`. Once it saves, you should see the words "hello world" appear in your console window. You should also see the red LED at the top of the board flash on and back off once per second. Don't worry about why the program works (we'll get to that in later exercises), just ensure you see the expected output from the LED and the console. If you don't see everything as expected, get help from the instructor or one of your neighbors to figure out what went wrong.

![green sticky note](images/sticky-note-green.png)


## Discussion

The board appears as a USB drive to your computer; this is how you are able to save files to it and read the contents of it using normal programs or your computer's operating system. In addition, it also can send and receive commands directly using a `tty`. TTY stands for "teletype", and the name harks from generations ago (in computer terms) before there were color screens and GUIs and network connections and other fancy ways to interact with computers.

Nope, in the old days, computers were connected using a serial cable, and the computer would send and receive characters via that connection. A teletype was any device that could send keystrokes (often using a loud clickityy-clacky keyboard) and display strings of output (often on a green screen). But a `tty` didn't have to be those things, it could be a modem, a printer (which would receive text to print and send back control characters to indicate status), or any number of other fancy hardware.

<img src="https://i.stack.imgur.com/P8GsV.jpg" style="max-width: 100%;" alt="asr-33 teletype">

The CPX uses the `tty` protocol to greatly simplify talking to the computer. It's already connected using a serial cable, and all modern operating systems have at least one program that speaks the primitive `tty` protocol, so no fancy software is necessary (though as mentioned above it's much easier on Windows to use Putty instead of the built-in serial tools).

The board listens for input on the `tty` connection and sends all output to the `tty`. This has no effect when you are not running a `tty` program, but when you are running such a program you can see what the board is doing and perform some basic control on the board. The primary use for our purposes is to view the output of `print()` calls and to interact with the debugger.


## References

* [Advanced Serial Console on Mac and Linux](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-mac-and-linux)
* [Advanced Serial Console on Windows](https://learn.adafruit.com/welcome-to-circuitpython/advanced-serial-console-on-windows)
* [Serial Terminal Basics](https://learn.sparkfun.com/tutorials/terminal-basics/command-line-windows-mac-linux)
* [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) (for Windows users)


<!-- begin auto-generated nav-links section -->
| Previous | Up | Next |
|:---------|:---:|-----:|
| [Installing/Updating CircuitPython](./setup_board.md) | [Setting Everything Up](./setup.md) | [Development Environment](./setup_environment.md) |
<!-- end auto-generated section -->
