#!/usr/bin/env python

# Exercise 6.
# Create some Note objects (...).
# Use both the regular and shorthand notations.

# Import pyknon from the git submodule in a subdirectory
import sys
sys.path.append('./pyknon')
from pyknon.music import Note

a = Note()
assert a.octave == 5
assert a.value == 0
assert a.volume == 100
assert a.dur == 0.25
assert a.midi_number == 60

b = Note(value=0, octave=5, dur=0.25, volume=127)
c = Note(0, 5, 0.25, 127)
assert b == c

assert str(Note(2)) == '<D>'
assert str(Note("D#")) == '<D#>'
assert str(Note("Eb8''")) == '<D#>'
assert Note("F#,").verbose == '<Note: 6, 4, 0.25>'
assert str(Note("C#", dur=2)) == '<C#>'

print 'OK'
