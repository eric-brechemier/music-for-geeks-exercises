#!/usr/bin/env python

# Exercise 9.
# Play with random_notes to generate different notes.
# Add different kinds of constraints and see which ones you like the best.

# We're using from __future__ import division,
# so we can type things like 1/4 instead of 0.25
from __future__ import division

# Import pyknon from the git submodule in a subdirectory
import sys
sys.path.append('./pyknon')
from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq

import collections
import math
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

def gen_midi(filename, note_list):
    midi = Midi(tempo=120)
    midi.seq_notes(note_list)
    midi.write(filename)

# weight for each value is computed from its offset from the middle of the
# list and the size of the list with the formula:
#   offset -> round( size * e^(-offset^2 / size) )
# where the amplifier increases the amplitude of values
# while the flattener flattens the curve of the bell shape
# (each defaults to the size of the list)
def gauss_weights(list, amplifier=None, flattener=None):
    size = len(list)
    if amplifier is None:
        amplifier = size
    if flattener is None:
        flattener = size

    middle = math.ceil(size/2)
    # When the number of items in the list is even,
    # position the middle between the two central values.
    if size % 2 == 0:
        middle += 0.5

    offset = middle - size
    weights = []
    for value in list:
        weight = round(amplifier * math.exp(-pow(offset, 2) / flattener))
        weights.append(weight)
        offset += 1

    return weights

weights7 = gauss_weights(range(1,8),10,10)
assert weights7 == [4, 7, 9, 10, 9, 7, 4], (
    "pre-computed weights expected for 7 values (*10,/10), was: %s" % weights7
)

weights7 = gauss_weights(range(1,8),21,3)
assert weights7 == [1, 6, 15, 21, 15, 6, 1], (
    "pre-computed weights expected for 7 values (*21,/3), was: %s" % weights7
)

weights4 = gauss_weights(range(1,5))
assert weights4 == [2, 4, 4, 2], (
    "pre-computed weights expected for a list of 4 values, was: %s" % weights4
)

# repeat each value in the list as many times as the weight at the same offset
def weight_list(list, weights):
    size = len(list)
    assert len(weights) >= size, "not enough weights for given list"
    result = []
    for i in range(size):
        value = list[i]
        times = int(weights[i])
        for t in range(times):
            result.append(value)
    return result

list1 = [1, 2, 3, 4, 5]
weights1 = [4, 2, 0, 3, 1]
weighted_list1 = weight_list(list1, weights1)
assert weighted_list1 == [1, 1, 1, 1, 2, 2, 4, 4, 4, 5], (
    "values in the list expected to be repeated according to weights, "
    "was: %s" % weighted_list1
)

def random_with_weights(scale, weights, filename):
    weighted_scale = weight_list(scale, weights)

    octaves = range(2,9)
    OCTAVES_GAUSS_AMPLIFIER = 21
    OCTAVES_GAUSS_FLATTENER = 3
    octave_weights = gauss_weights(octaves,
                                   OCTAVES_GAUSS_AMPLIFIER,
                                   OCTAVES_GAUSS_FLATTENER)
    weighted_octaves = weight_list(octaves, octave_weights)

    durations = [1/64, 1/32, 1/16, 1/8, 1/4, 1/2, 1]
    DURATIONS_GAUSS_AMPLIFIER = 100
    DURATIONS_GAUSS_FLATTENER = 3
    durations_weights = gauss_weights(durations,
                                      DURATIONS_GAUSS_AMPLIFIER,
                                      DURATIONS_GAUSS_FLATTENER)
    weighted_durations = weight_list(durations, durations_weights)

    NUMBER_OF_NOTES = 100
    notes = random_notes(weighted_scale,
                         weighted_octaves,
                         weighted_durations,
                         NUMBER_OF_NOTES)
    gen_midi(filename, notes)

# See details and references about scales in exercise8.py
# C Major: C, D, E, F, G, A, B
MAJOR_SCALE = [0, 2, 4, 5, 7, 9, 11]
# A minor harmonic: A, B, C, D, E, F, G#
HARMONIC_MINOR_SCALE = [9, 11, 0, 2, 4, 5, 8]
# A (ascending) melodic minor: A, B, C, D, E, F#, G#
MELODIC_MINOR_SCALE = [9, 11, 0, 2, 4, 6, 8]
# C Major pentatonic scale: C, D, E, G, A
PENTATONIC_SCALE = [0, 2, 4, 7, 9]

# Emphasize notes in groups doubling weights from one group to the next
# C (8)
# G (4) F (4)
# E (2) A (2)
# D (1) B (1)
GEOMETRIC_WEIGHTS = [8, 1, 2, 4, 4, 2, 1]

random_with_weights(MAJOR_SCALE,
                    GEOMETRIC_WEIGHTS,
                    'exercise9-major-geometric-weights.mid')

