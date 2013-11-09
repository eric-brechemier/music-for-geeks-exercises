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
from random import choice, randint

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

# weight for each value is computed from its offset
# with the formula:
#   offset -> round( amplifier * e^(-offset^2 / flattener) )
# where the amplifier increases the amplitude of values
# while the flattener flattens the curve of the bell shape.
#
# The offset 0 corresponds to the item with highest weight,
# the position of the top of the Gauss curve. A positive offset
# pushes the curve to the right, a negative offset pulls the curve
# to the left. The offset defaults to the middle of the list,
# which falls between two values when the number of items is even.
def gauss_weights(list, amplifier=None, flattener=None, offset=None):
    size = len(list)
    if amplifier is None:
        amplifier = size
    if flattener is None:
        flattener = size

    if offset is None:
        middle = math.ceil(size/2)
        # When the number of items in the list is even,
        # position the middle between the two central values.
        if size % 2 == 0:
            middle += 0.5
        offset = size - middle

    weights = []
    for value in list:
        weight = round(amplifier * math.exp(-pow(offset, 2) / flattener))
        weights.append(weight)
        offset -= 1

    return weights

weights7 = gauss_weights(range(1, 8), 10, 10)
assert weights7 == [4, 7, 9, 10, 9, 7, 4], (
    "pre-computed weights expected for 7 values (*10,/10), was: %s" % weights7
)

weights7 = gauss_weights(range(1, 8), 21, 3)
assert weights7 == [1, 6, 15, 21, 15, 6, 1], (
    "pre-computed weights expected for 7 values (*21,/3), was: %s" % weights7
)

weights4 = gauss_weights(range(1, 5))
assert weights4 == [2, 4, 4, 2], (
    "pre-computed weights expected for a list of 4 values, was: %s" % weights4
)

weights4 = gauss_weights(range(1, 5), 10, 10, 0)
assert weights4 == [10, 9, 7, 4], (
    "shifted weights expected for 4 values (*10,/10,+0), was: %s" % weights4
)

weights4 = gauss_weights(range(1, 5), 10, 10, 1)
assert weights4 == [9, 10, 9, 7], (
    "shifted weights expected for 4 values (*10,/10,+1), was: %s" %
    weights4
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

# pick a position in the given array,
# an integer between 0 and len(size)-1,
# using each value as a weight in the selection:
# value 20 weights 20 times more in the selection than value 1
def weighted_random(weights):
    assert len(weights) > 0, 'list of weights must not be empty'
    total = sum(weights)
    selected = randint(0, total)
    current = 0
    for offset in range(0, len(weights)):
        current += weights[offset]
        if selected <= current:
            return offset

# memory_weights indicates the weight for reusing the property of a note:
# * item 0 gives the weight for a new note (no reuse)
# * item i gives the weight for the i-th note previously played
# The memory weights apply to octaves and durations only.
def random_notes_with_memory(pitch_list, octave_list, duration_list,
                             number_of_notes, memory_weights, volume=120):
    assert len(memory_weights) > 1, "more than 1 weight expected for memory"
    result = NoteSeq()
    for offset in range(0, number_of_notes):
        pitch = choice(pitch_list)

        if 1+offset >= len(memory_weights):
            weights = memory_weights
        else:
            weights = memory_weights[0:1+offset]
        octave_selection = weighted_random(weights)
        if octave_selection == 0: # new note
            octave = choice_if_list(octave_list)
        else: # previous note at given position starting from the end
            octave = result[-octave_selection].octave

        duration_selection = weighted_random(weights)
        if duration_selection == 0: # new note
            dur = choice_if_list(duration_list)
        else: # previous note at given position starting from the end
            dur = result[-octave_selection].dur

        vol = choice_if_list(volume)
        result.append(Note(pitch, octave, dur, vol))
    return result

def random_with_weights_and_memory(scale, weights, filename):
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
    # first 8 non-zero values of Fibonacci sequence, from last to first
    MEMORY_WEIGHTS = [21, 13, 8, 5, 3, 2, 1, 1]
    notes = random_notes_with_memory(weighted_scale,
                                     weighted_octaves,
                                     weighted_durations,
                                     NUMBER_OF_NOTES,
                                     MEMORY_WEIGHTS)
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

random_with_weights(HARMONIC_MINOR_SCALE,
                    GEOMETRIC_WEIGHTS,
                    'exercise9-minor-harmonic-geometric-weights.mid')

random_with_weights(MELODIC_MINOR_SCALE,
                    GEOMETRIC_WEIGHTS,
                    'exercise9-minor-melodic-geometric-weights.mid')

random_with_weights_and_memory(
    MAJOR_SCALE,
    GEOMETRIC_WEIGHTS,
    'exercise9-major-geometric-weights-and-memory.mid'
)

random_with_weights_and_memory(
    HARMONIC_MINOR_SCALE,
    GEOMETRIC_WEIGHTS,
    'exercise9-minor-harmonic-geometric-weights-and-memory.mid'
)

random_with_weights_and_memory(
    MELODIC_MINOR_SCALE,
    GEOMETRIC_WEIGHTS,
    'exercise9-minor-melodic-geometric-weights-and-memory.mid'
)
