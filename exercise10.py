#!/usr/bin/env python

# Exercise 10.
# Input your favorite integer sequence in play_list and see how it sounds.
# If you don't have a favorite integer sequence, go to the On-Line Encyclopedia
# of Integer Sequences (https://oeis.org/) and pick one.

# We're using from __future__ import division,
# so we can type things like 1/4 instead of 0.25
from __future__ import division

# Import pyknon from the git submodule in a subdirectory
import sys
sys.path.append('./pyknon')
from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq

import collections
import itertools
import math
from random import choice, randint

def choice_if_list(item):
    if isinstance(item, collections.Iterable):
        return choice(item)
    else:
        return item

def gen_midi(filename, note_list):
    midi = Midi(tempo=120)
    midi.seq_notes(note_list)
    midi.write(filename)

def fibonacci(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

# http://blog.yjl.im/2011/01/generating-pascals-triangle-using.html
def pascals_triangle(n):
    x = [1]
    yield x
    for i in range(n - 1):
        x = [sum(i) for i in zip([0] + x, x + [0])]
        yield x

def flatten(iterable):
    return list(itertools.chain.from_iterable(iterable))

def play_list(pitch_list, octave_list, duration, volume=120):
    result = NoteSeq()
    for pitch in pitch_list:
        note = pitch % 12
        octave = choice_if_list(octave_list)
        dur = choice_if_list(duration)
        vol = choice_if_list(volume)
        result.append(Note(note, octave, dur, vol))
    return result

def random_fib():
    octave = range(5, 7)
    fib = fibonacci(100000000000)
    pascal = flatten(pascals_triangle(30))

    n1 = play_list(fib, octave, 1/16)
    n2 = play_list(pascal, 4, 1/16)
    n3 = play_list(pascal, octave, 1/16)

    gen_midi("exercise10-fibonacci.mid", n1)
    gen_midi("exercise10-pascal.mid", n2)
    gen_midi("exercise10-pascal_octaves.mid", n3)

random_fib()
