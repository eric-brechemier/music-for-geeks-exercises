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

# Variations on Regular Notation
assert Note().verbose == '<Note: 0, 5, 0.25>'
assert Note(value=9).verbose == '<Note: 9, 5, 0.25>'
assert Note(octave=7).verbose == '<Note: 0, 7, 0.25>'
assert Note(dur=0.5).verbose == '<Note: 0, 5, 0.5>'
assert Note(volume=42).volume == 42

note1234 = Note(1,2,3,4)
assert note1234.value == 1
assert note1234.octave == 2
assert note1234.dur == 3
assert note1234.volume == 4

note4321 = Note(volume=1,dur=2,octave=3,value=4)
assert note4321.value == 4
assert note4321.octave == 3
assert note4321.dur == 2
assert note4321.volume == 1

# Variations on Shorthand Notation
assert Note('A').verbose == '<Note: 9, 5, 0.25>'
assert Note('C').verbose == '<Note: 0, 5, 0.25>'
assert Note('A#').verbose == '<Note: 10, 5, 0.25>'
assert Note('Ab').verbose == '<Note: 8, 5, 0.25>'

assert Note('A\'').verbose == '<Note: 9, 5, 0.25>'
assert Note("A''").verbose == '<Note: 9, 6, 0.25>'
assert Note("A''''''").verbose == '<Note: 9, 10, 0.25>'
assert Note("A,").verbose == '<Note: 9, 4, 0.25>'
assert Note("A,,").verbose == '<Note: 9, 3, 0.25>'
assert Note("A,,,,,").verbose == '<Note: 9, 0, 0.25>'

assert Note('A8').verbose == '<Note: 9, 5, 0.125>'
assert Note('A4').verbose == '<Note: 9, 5, 0.25>'
assert Note('A2').verbose == '<Note: 9, 5, 0.5>'
assert Note('A1').verbose == '<Note: 9, 5, 1.0>'

assert Note('A#5,,').verbose == '<Note: 10, 3, 0.2>'

print 'OK'
