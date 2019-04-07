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

# Q. In the following code, what is the order of the notes in the MIDI file?
midi = Midi()
midi.seq_notes(seq1)
midi.seq_notes(seq2)
# A. both seq1 and seq2 are written to the same track (1).
#    The notes of seq2 sequence override notes at the same position in seq1.
midi.write("exercise07-F-G-A.mid")

# Q. What happens when you change the second-to-last line to
#    midi.seq_notes(seq2, time=3)
midi = Midi()
midi.seq_notes(seq1)
midi.seq_notes(seq2, time=3)
# A. Now the sequence seq2 is offset by 3 beats,
#    the two sequences seq1 and seq2 appear concatenated.
midi.write("exercise07-C-D-E-F-G-A.mid")

# Q. What happens when you change the second-to-last line to
#    midi.seq_notes(seq2, time=4)
midi = Midi()
midi.seq_notes(seq1)
midi.seq_notes(seq2, time=4)
# A. Now the sequence seq2 is offset by 4 beats,
#    the two sequences seq1 and seq2 appear concatenated,
#    with a rest of 1 beat in between.
midi.write("exercise07-C-D-E-R-F-G-A.mid")
