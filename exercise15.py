#!/usr/bin/env python

# Exercise 15.
# Try to construct a scale using only frequencies from the harmonic series.
# Notice how it sounds different from the equal temperament.

from math import log

SEMITONE = 1.059463
NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

def freq_to_note(x):
    interval = int(round(log(x/440.0, SEMITONE))) % 12
    return NOTES[interval]

def note_to_freq(n):
    if n in NOTES:
        return 440 * (SEMITONE ** NOTES.index(n))

assert freq_to_note(440) == 'A'
assert freq_to_note(442) == 'A'
assert freq_to_note(449) == 'A'
assert freq_to_note(455) == 'A#'

assert note_to_freq('A#') == 466.16372

def harmonic_series(n, fundamental):
    return [fundamental * (x + 1) for x in range(n)]

assert harmonic_series(13,55) == \
       [55, 110, 165, 220, 275, 330, 385, 440, 495, 550, 605, 660, 715]

# > Notice how it sounds different from the equal temperament.
# See exercise15.sh which generates a WAV file for this harmonic series,
# defined in the Csound score exercise15-csound.sco.

print "OK"
