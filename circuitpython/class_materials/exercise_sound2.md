
## Time Box

25 minutes


## Overview

Now that you understand basic tone playing, build that into tune playing.  

## What to Do

Enter the following program in your editor:

```python
# Sound Demo
# Pay a tune from a list of note tuples.
# A4 (Middle A) = 440Hz
# freq = f0 * a**n #n = half-steps from base, a = 2**(1/12)

from adafruit_circuitplayground.express import cpx
import time

class duration:
#Shorthand notation to make it easier to type note lengths, but keep it in a namespace.

    _duration = 0
    def __init__(self, tempo=60):
        self._duration = 60/tempo * .25 # quarter note duration in seconds
        self.e = self._duration / 2 # eighth note
        self.s = self._duration / 4 # sixteenth note
        self.q = self._duration # quarter
        self.h = self._duration * 2 # half
        self.w = self._duration * 4 # whole

# This part can be re-used, or the contents of frequencies{} hard-coded for other apps.
# ------------------------------------------------------------------
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
half_steps = {notes[i]:i for i in range(len(notes))}
octaves = list(range(3,6))
factor = 2**(1/12) # frequency change factor per half-step
base = 4 # Base octave

def get_frequency(note, octave):
    offset = half_steps[note] + 12*(octave - base)
    frequency = 440 * factor**offset #A4 is baseline frequency
    return frequency

frequencies = {note + str(octave): get_frequency(note, octave) for note in notes for octave in octaves}
# ------------------------------------------------------------------

### Define tunes ###
d = duration()
#Row your boat
rowyourboat = [('C3', d.q),('C3', d.q), ('C3', d.q), ('D3', d.s), ('E3', d.q)]

# Mary had a little lamb
littlelamb = [('E4',d.q),('D4',d.q),('C4',d.q),('D4',d.q),('E4',d.e), ('E4',d.e), ('E4',d.q)]

playing = False

while True:
    if cpx.button_a:
        playing = True
        tune = rowyourboat
    if cpx.button_b:
        playing = True
        tune = littlelamb
    if playing:
        note_count = len(tune)
        for note in tune:
            if note[0] in frequencies:
                print(note)
                cpx.play_tone(frequencies[note[0]], note[1])
            else:
                pass
                # ToDo: rests
        playing = False

# ToDo: Add capability for rests; include flats in frequencies.
```

Save the program on your CPX as `code.py`. Once it saves, you should be to play the tones by pressing button A.

![green sticky note](images/sticky-note-green.png)


## Deep Dive

As explained in the sound1 exercise, notes have a mathematical relationship.  Generating a dictionary of frequencies allows one to program tunes by creating a list of the note tuples consisting of the Note (name and octave) and its duration.  

Any non-trivial tune will also include quiet "rest" beats, which is left as an exercise.

### Frequencies (repeated from sound1 exercise)
Musical note frequencies have a mathematical relationship.  "Middle-C" is also known as "C4" (C in the 4th octave).  A4 (440Hz) is often used as a reference point for calculating other frequencies. Doubling the frequency raises the note 1 octave.  There are 12 notes in the chromatic scale, thus, to calculate a note's frequency:

    a = 2**(1/12)
    fn = f0 * a**n 
    where
    f0 = the frequency of one fixed note which must be defined. A common choice is setting the A     above middle C (A4) at f0 = 440 Hz.
    n = the number of half steps away from the fixed note you are. If you are at a higher note, n is     positive. If you are on a lower note, n is negative.
    fn = the frequency of the note n half steps away.
    a = (2)**1/12 = the twelth root of 2 = the number which when multiplied by itself 12 times equals 2 = 1.059463094359... 


## Experience Points

* Flesh-out the rest of the tunes.

* Add rests to the tune and play routine. Consider an inner loop or function that uses time.monotonic() and time.sleep() to count the duration.

* Try using cpx.start_tone(freq), cpx.stop_tone(freq), and using time.monotonic() to control duration of the tone. 

## Resources

* [Docs » adafruit_circuitplayground.express](https://circuitpython.readthedocs.io/projects/circuitplayground/en/latest/api.html)
* [Play Tone docs](https://circuitpython.readthedocs.io/projects/circuitplayground/en/latest/_modules/adafruit_circuitplayground/express.html#Express.play_tone)
* [Frequency Calculations](https://pages.mtu.edu/~suits/NoteFreqCalcs.html)
