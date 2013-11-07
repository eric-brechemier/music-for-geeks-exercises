#!/usr/bin/env python

# Exercise 8.
# Generate some random notes using random1, random2, and random3
# but using the major and minor scales.

# We're using from __future__ import division,
# so we can type things like 1/4 instead of 0.25
from __future__ import division

# Import pyknon from the git submodule in a subdirectory
import sys
sys.path.append('./pyknon')
from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq

import collections
from random import choice

def choice_if_list(item):
    if isinstance(item, collections.Iterable):
        return choice(item)
    else:
        return item

def random_notes(pitch_list, octave_list, duration,
                 number_of_notes, volume=120):
    result = NoteSeq()
    for x in range(0, number_of_notes):
        pitch = choice(pitch_list)
        octave = choice_if_list(octave_list)
        dur = choice_if_list(duration)
        vol = choice_if_list(volume)
        result.append(Note(pitch, octave, dur, vol))
    return result

CHROMATIC_SCALE = range(0, 12)
PENTATONIC_SCALE = [0, 2, 4, 7, 9]

def is_chromatic(notes):
    for note in notes:
        if not note.value in CHROMATIC_SCALE:
            return False
    return True

def is_pentatonic(notes):
    for note in notes:
        if not note.value in PENTATONIC_SCALE:
            return False
    return True

MIN_OCTAVE = 0
MAX_OCTAVE = 10

def min_octave(notes):
    result = MAX_OCTAVE
    for note in notes:
        result = min(result, note.octave)
    return result

def max_octave(notes):
    result = MIN_OCTAVE
    for note in notes:
        result = max(result, note.octave)
    return result

def is_every_note_duration_in(notes, durations):
    for note in notes:
        if not note.dur in durations:
            return False
    return True

notes1 = random_notes(range(0, 12), range(5, 7), [0.25, 0.5, 1], 5)
assert (
        len(notes1) == 5 and
        is_chromatic(notes1) and
        min_octave(notes1) >= 5 and max_octave(notes1) <= 6 and
        is_every_note_duration_in(notes1, [0.25, 0.5, 1])
    ), (
    "we want to generate five notes "
    "from the chromatic scale, "
    "in any octave from five to six, "
    "with quarter note, half note or whole note durations, "
    "was: %s" % (notes1.verbose)
)

notes2 = random_notes([0, 2, 4, 7, 9], 5, 0.5, 5)
assert (
        len(notes2) == 5 and
        is_pentatonic(notes2) and
        min_octave(notes2) == 5 and max_octave(notes2) == 5 and
        is_every_note_duration_in(notes2, [0.5])
    ), (
    "we want to generate five notes "
    "from the pentatonic scale, "
    "in the central octave, "
    "with a duration of a half note, "
    "was: %s" % (notes1.verbose)
)

def gen_midi(filename, note_list):
    midi = Midi(tempo=120)
    midi.seq_notes(note_list)
    midi.write(filename)

def random1(scale, filename):
    durations = [1/64, 1/32, 1/16, 1/8, 1/4, 1/2, 1]
    notes = random_notes(scale,
                         range(0, 9),
                         durations,
                         100,
                         range(0, 128, 20))
    gen_midi(filename, notes)

def random2(scale, filename):
    notes = random_notes(scale,
                         range(3, 7),
                         [1/16, 1/8],
                         100)
    gen_midi(filename, notes)

def random3(scale, filename):
    pentatonic = [0, 2, 4, 7, 9]
    notes = random_notes(scale,
                         range(5, 7),
                         1/16,
                         100)
    gen_midi(filename, notes)

random1(CHROMATIC_SCALE, 'exercise8-random1-chromatic.mid')
random2(CHROMATIC_SCALE, 'exercise8-random2-chromatic.mid')
random3(PENTATONIC_SCALE, 'exercise8-random3-pentatonic.mid')
