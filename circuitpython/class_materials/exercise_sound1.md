
## Time Box

15 minutes


## Overview

The board has a speaker that can play tones or .wav files.  By setting the frequencies and durations, one can play a simple monotonic tune, or one can use a series of .wav files to play sound effects to go with other cpx interactions.

## What to Do

Enter the following program in your editor:

```python
from adafruit_circuitplayground.express import cpx
import time

A4 = 440
base = 2**(1/12)
A3 = A4 * base**-12 # 12 half steps down
A5 = A4 * base**12 # up
playing = False

print('Entering program loop. Press button A to play tones.')
while  True:
    if cpx.button_a:
        playing = True
    
    if playing:
        cpx.play_tone(A4,1)
        print(A4)
        cpx.play_tone(A3, 1)
        print(A3)
        cpx.play_tone(A5, 1)
        print(A4)
        playing = False
```

Save the program on your CPX as `code.py`. Once it saves, you should be to play the tones by pressing button A.

![green sticky note](images/sticky-note-green.png)


## Deep Dive

You can use a timer (time.monotonic()), cpx.start_tone(freq) and cpx.stop_tone() to gain some further control on sounds.

### Frequencies
Musical note frequencies have a mathematical relationship.  "Middle-C" is also known as "C4" (C in the 4th octave).  A4 (440Hz) is often used as a reference point for calculating other frequencies. Doubling the frequency raises the note 1 octave.  There are 12 notes in the chromatic scale, thus, to calculate a note's frequency:

    a = 2**(1/12)
    fn = f0 * a**n 
    where
    f0 = the frequency of one fixed note which must be defined. A common choice is setting the A     above middle C (A4) at f0 = 440 Hz.
    n = the number of half steps away from the fixed note you are. If you are at a higher note, n is     positive. If you are on a lower note, n is negative.
    fn = the frequency of the note n half steps away.
    a = (2)**1/12 = the twelth root of 2 = the number which when multiplied by itself 12 times equals 2 = 1.059463094359... 


## Experience Points

* Build a generalized tune player, including multiple octaves of notes, common note durations, and rests.

* Try using cpx.start_tone(freq), cpx.stop_tone(freq), and using time.monotonic() to control duration of the tone. 

## Resources

* [Docs » adafruit_circuitplayground.express](https://circuitpython.readthedocs.io/projects/circuitplayground/en/latest/api.html)
* [Play Tone](https://circuitpython.readthedocs.io/projects/circuitplayground/en/latest/_modules/adafruit_circuitplayground/express.html#Express.play_tone)
* [Frequency Calculations](https://pages.mtu.edu/~suits/NoteFreqCalcs.html)


