<!-- begin auto-generated title section -->
<!-- end auto-generated section -->


## Time Box

10 minutes


## Overview

In this section we will set up [Arduino](https://www.arduino.cc/en/Main/Software) and [Visual Studio Code](https://code.visualstudio.com/) (and talk about other editors you can use instead) and connect to the CPX from within the editor environment.

**Note:** everything in this section is optional; if you already have an editor you like, use it!


## What to Do

[Download](https://code.visualstudio.com/download) and install Visual Studio Code.

Once it's installed, open it. On the left side of the main window, go to the extensions tool (click the icon on the left of the main window that looks like a square with a missing piece). Search for and install the following extensions:

* Python (`ms-python-python`): the primary extension for working with Python source code
* Arduino (`vsciot-vs-code.vscode-arduino`): this extension allows you to enable debugging within the editor

To use the Arduino extension, you also need to install [the Arduino IDE](https://www.arduino.cc/en/Main/Software). You won't ever need to run it, just have it installed so that VS Code can run some of the tools it installs.

We need to configure how VS Code understands finding your board. To do this, the fastest way is to find where VS Code keeps your overall user preferences. On MacOS this folder is in your home directory and it's called `.vscode`. Inside that folder, create a file called `arduino.json` and put give it the contents from the right section below:


### MacOS

<img src="./images/icon-mac.png" height="50" alt="macos logo">

```json
{
    "path": "/Applications",
    "commandPath": "Contents/MacOS/run-arduino.sh",
    "board": "arduino:avr:circuitplay32u4cat",
    "port": "/dev/tty.usbmodemN"
}
```

**Note:** use the `tty` connection we found in the last exercise.


### Windows

<img src="./images/icon-windows.jpg" height ="50" alt="windows logo">

```json
{
    "path": "C:/Program Files (x86)/Arduino",
    "commandPath": "arduino_debug.exe",
    "board": "arduino:avr:circuitplay32u4cat",
    "port": "COMn"
}
```
**Note:** use the `COM` connection we found in the last exercise.


### Linux

<img src="./images/icon-linux.jpg" height ="50" alt="linux logo">

**TODO**

### Everyone

Now that you have Arduino and VS Code set up, open 

#TODO


## Discussion

Luckily, your CPX board doesn't require any special software in order to work; just a computer, a USB cable, and any program that lets you edit text files are enough.

That program, though... it's nice to have one that helps you to some extent rather than just using `vim`. We need an Editor.


### Editor or IDE?

What is an IDE? That stands for Integrated Development Environment, and it means a program that gives you lots of tooling and functionality related to writing code. While an IDE and an editor can look a lot alike, there are some fundamental differences that you should be familiar with:

* IDEs usually have debugging and analysis tools built-in
* IDEs typically are specific to one language (or a small set of related languages)
* IDEs often are *monolithic*, meaning they are large programs that try to do a lot of things

In the early days of writing software, IDEs didn't exist. That changed with the advent of GUI-based operating systems (like the original Mac OS and Windows 95), when suddenly it was possible to put all the tooling and functionality that a developer needed into a single program with a well-defined idea about how software should be written, built, tested/debugged, and deployed.

If you've used any of the following, you've used an IDE:

* [Visual Studio](https://visualstudio.microsoft.com/) (by far the most famous/infamous)
* [XCode](https://developer.apple.com/xcode/)
* [Eclipse](https://www.eclipse.org/)
* [Android Studio](https://developer.android.com/studio)
* [PyCharm](https://www.jetbrains.com/pycharm/)
* [Mu](https://codewith.mu/)

Over the years, IDEs have become much more powerful and feature-rich ... but at a cost. IDEs generally take much longer to start than simple editors, and they are very memory- and CPU-intensive.


### Visual Studio Code

While I don't usually promote specific software products or tools, there are a couple exceptions. For editing text, that recommendation is [Visual Studio Code](https://code.visualstudio.com/).

Basically, it's lightweight (it loads in under a second), it's visually comfortable, and most of all it's got many of the most significant advantages of an IDE without the slowness of one. It is extensible, so as it sees what kinds of files you work with, it recommends plugins to better serve the needs of working in those files.

VS Code also has the ability to run a terminal session inside the application; this enables live debugging on the device without having to also have a separate terminal open. That's the main thing we set up above.


### Other Options

Besides the IDEs listed above, you can use any editor you want: `vim`, `nano`, `emacs`, TextWrangler, Notepad++, ... the list goes on.


### Other Software

None! Part of what makes `circuitpython` so elegant is that no specialied tools are ever needed. All you do to replace the running program on the device is save your code as `code.py` on the USB drive associated with the board.

**Note:** `circuitpython` can also handle a program file if it is named `main.py`, and there is a [specific set of rules it follows](https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code#naming-your-program-file-7-32) if there are files with both names; for simplicity and by convention, just always name your primary program `code.py`.



## References

* [Python IDEs and Code Editors (Guide)](https://realpython.com/python-ides-code-editors-guide/)


<!-- begin auto-generated nav-links section -->
<!-- end auto-generated section -->
