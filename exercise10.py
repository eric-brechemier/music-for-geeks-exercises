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

def gen_fib():
    octave = range(5, 7)
    fib = fibonacci(100000000000)

    print "Generate %i notes based on Fibonacci sequence" % len(fib)
    n1 = play_list(fib, octave, 1/16)

    gen_midi("exercise10-fibonacci.mid", n1)

def gen_pascal():
    octave = range(5, 7)
    pascal = flatten(pascals_triangle(30))

    print "Generate %i notes based on Pascal's triangles" % len(pascal)
    n2 = play_list(pascal, 4, 1/16)
    n3 = play_list(pascal, octave, 1/16)

    gen_midi("exercise10-pascal.mid", n2)
    gen_midi("exercise10-pascal-octaves.mid", n3)

# I chose the sequence of differences between consecutive primes
# https://oeis.org/A001223

# 1,000 first values in the sequence, taken from:
# "First 10,000 terms", by N. J. A. Sloane
# https://oeis.org/A001223/b001223.txt
# by running:
# ./data/sequence-to-array.sh data/b001223.txt 10 1000
PRIME_DIFF = [
    1, 2, 2, 4, 2, 4, 2, 4, 6, 2,
    6, 4, 2, 4, 6, 6, 2, 6, 4, 2,
    6, 4, 6, 8, 4, 2, 4, 2, 4, 14,
    4, 6, 2, 10, 2, 6, 6, 4, 6, 6,
    2, 10, 2, 4, 2, 12, 12, 4, 2, 4,
    6, 2, 10, 6, 6, 6, 2, 6, 4, 2,
    10, 14, 4, 2, 4, 14, 6, 10, 2, 4,
    6, 8, 6, 6, 4, 6, 8, 4, 8, 10,
    2, 10, 2, 6, 4, 6, 8, 4, 2, 4,
    12, 8, 4, 8, 4, 6, 12, 2, 18, 6,
    10, 6, 6, 2, 6, 10, 6, 6, 2, 6,
    6, 4, 2, 12, 10, 2, 4, 6, 6, 2,
    12, 4, 6, 8, 10, 8, 10, 8, 6, 6,
    4, 8, 6, 4, 8, 4, 14, 10, 12, 2,
    10, 2, 4, 2, 10, 14, 4, 2, 4, 14,
    4, 2, 4, 20, 4, 8, 10, 8, 4, 6,
    6, 14, 4, 6, 6, 8, 6, 12, 4, 6,
    2, 10, 2, 6, 10, 2, 10, 2, 6, 18,
    4, 2, 4, 6, 6, 8, 6, 6, 22, 2,
    10, 8, 10, 6, 6, 8, 12, 4, 6, 6,
    2, 6, 12, 10, 18, 2, 4, 6, 2, 6,
    4, 2, 4, 12, 2, 6, 34, 6, 6, 8,
    18, 10, 14, 4, 2, 4, 6, 8, 4, 2,
    6, 12, 10, 2, 4, 2, 4, 6, 12, 12,
    8, 12, 6, 4, 6, 8, 4, 8, 4, 14,
    4, 6, 2, 4, 6, 2, 6, 10, 20, 6,
    4, 2, 24, 4, 2, 10, 12, 2, 10, 8,
    6, 6, 6, 18, 6, 4, 2, 12, 10, 12,
    8, 16, 14, 6, 4, 2, 4, 2, 10, 12,
    6, 6, 18, 2, 16, 2, 22, 6, 8, 6,
    4, 2, 4, 8, 6, 10, 2, 10, 14, 10,
    6, 12, 2, 4, 2, 10, 12, 2, 16, 2,
    6, 4, 2, 10, 8, 18, 24, 4, 6, 8,
    16, 2, 4, 8, 16, 2, 4, 8, 6, 6,
    4, 12, 2, 22, 6, 2, 6, 4, 6, 14,
    6, 4, 2, 6, 4, 6, 12, 6, 6, 14,
    4, 6, 12, 8, 6, 4, 26, 18, 10, 8,
    4, 6, 2, 6, 22, 12, 2, 16, 8, 4,
    12, 14, 10, 2, 4, 8, 6, 6, 4, 2,
    4, 6, 8, 4, 2, 6, 10, 2, 10, 8,
    4, 14, 10, 12, 2, 6, 4, 2, 16, 14,
    4, 6, 8, 6, 4, 18, 8, 10, 6, 6,
    8, 10, 12, 14, 4, 6, 6, 2, 28, 2,
    10, 8, 4, 14, 4, 8, 12, 6, 12, 4,
    6, 20, 10, 2, 16, 26, 4, 2, 12, 6,
    4, 12, 6, 8, 4, 8, 22, 2, 4, 2,
    12, 28, 2, 6, 6, 6, 4, 6, 2, 12,
    4, 12, 2, 10, 2, 16, 2, 16, 6, 20,
    16, 8, 4, 2, 4, 2, 22, 8, 12, 6,
    10, 2, 4, 6, 2, 6, 10, 2, 12, 10,
    2, 10, 14, 6, 4, 6, 8, 6, 6, 16,
    12, 2, 4, 14, 6, 4, 8, 10, 8, 6,
    6, 22, 6, 2, 10, 14, 4, 6, 18, 2,
    10, 14, 4, 2, 10, 14, 4, 8, 18, 4,
    6, 2, 4, 6, 2, 12, 4, 20, 22, 12,
    2, 4, 6, 6, 2, 6, 22, 2, 6, 16,
    6, 12, 2, 6, 12, 16, 2, 4, 6, 14,
    4, 2, 18, 24, 10, 6, 2, 10, 2, 10,
    2, 10, 6, 2, 10, 2, 10, 6, 8, 30,
    10, 2, 10, 8, 6, 10, 18, 6, 12, 12,
    2, 18, 6, 4, 6, 6, 18, 2, 10, 14,
    6, 4, 2, 4, 24, 2, 12, 6, 16, 8,
    6, 6, 18, 16, 2, 4, 6, 2, 6, 6,
    10, 6, 12, 12, 18, 2, 6, 4, 18, 8,
    24, 4, 2, 4, 6, 2, 12, 4, 14, 30,
    10, 6, 12, 14, 6, 10, 12, 2, 4, 6,
    8, 6, 10, 2, 4, 14, 6, 6, 4, 6,
    2, 10, 2, 16, 12, 8, 18, 4, 6, 12,
    2, 6, 6, 6, 28, 6, 14, 4, 8, 10,
    8, 12, 18, 4, 2, 4, 24, 12, 6, 2,
    16, 6, 6, 14, 10, 14, 4, 30, 6, 6,
    6, 8, 6, 4, 2, 12, 6, 4, 2, 6,
    22, 6, 2, 4, 18, 2, 4, 12, 2, 6,
    4, 26, 6, 6, 4, 8, 10, 32, 16, 2,
    6, 4, 2, 4, 2, 10, 14, 6, 4, 8,
    10, 6, 20, 4, 2, 6, 30, 4, 8, 10,
    6, 6, 8, 6, 12, 4, 6, 2, 6, 4,
    6, 2, 10, 2, 16, 6, 20, 4, 12, 14,
    28, 6, 20, 4, 18, 8, 6, 4, 6, 14,
    6, 6, 10, 2, 10, 12, 8, 10, 2, 10,
    8, 12, 10, 24, 2, 4, 8, 6, 4, 8,
    18, 10, 6, 6, 2, 6, 10, 12, 2, 10,
    6, 6, 6, 8, 6, 10, 6, 2, 6, 6,
    6, 10, 8, 24, 6, 22, 2, 18, 4, 8,
    10, 30, 8, 18, 4, 2, 10, 6, 2, 6,
    4, 18, 8, 12, 18, 16, 6, 2, 12, 6,
    10, 2, 10, 2, 6, 10, 14, 4, 24, 2,
    16, 2, 10, 2, 10, 20, 4, 2, 4, 8,
    16, 6, 6, 2, 12, 16, 8, 4, 6, 30,
    2, 10, 2, 6, 4, 6, 6, 8, 6, 4,
    12, 6, 8, 12, 4, 14, 12, 10, 24, 6,
    12, 6, 2, 22, 8, 18, 10, 6, 14, 4,
    2, 6, 10, 8, 6, 4, 6, 30, 14, 10,
    2, 12, 10, 2, 16, 2, 18, 24, 18, 6,
    16, 18, 6, 2, 18, 4, 6, 2, 10, 8,
    10, 6, 6, 8, 4, 6, 2, 10, 2, 12,
    4, 6, 6, 2, 12, 4, 14, 18, 4, 6,
    20, 4, 8, 6, 4, 8, 4, 14, 6, 4,
    14, 12, 4, 2, 30, 4, 24, 6, 6, 12,
    12, 14, 6, 4, 2, 4, 18, 6, 12, 8
]

def gen_prime_diff():
    octave = range(5, 7)
    duration = 1/16

    print (
      "Generate %i notes based on differences between primes" % len(PRIME_DIFF)
    )
    sequence = play_list(PRIME_DIFF, octave, duration)
    gen_midi("exercise10-prime-differences.mid", sequence)

gen_fib()
gen_pascal()
gen_prime_diff()
