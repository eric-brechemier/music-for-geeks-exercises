#!/usr/bin/env python

# Exercise 7.
# In the following code, what is the order of the notes in the MIDI file?
# What happens when you change the second-to-last line to
#   midi.seq_notes(seq2, time=3)
# or
#   midi.seq_notes(seq2, time=4)

# Import pyknon from the git submodule in a subdirectory
import sys
sys.path.append('./pyknon')
from pyknon.genmidi import Midi
from pyknon.music import NoteSeq

seq1 = NoteSeq("C D E")
seq2 = NoteSeq("F G A")

midi = Midi()
midi.seq_notes(seq1)
midi.seq_notes(seq2)
midi.write("foo.mid")
