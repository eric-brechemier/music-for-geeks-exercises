#!/usr/bin/env python

# Exercise 11.
# Create your own crab canon using the function crab_canon.

# Import pyknon from the git submodule in a subdirectory
import sys
sys.path.append('./pyknon')
from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq

def crab_canon():
    theme2 = NoteSeq("file://exercise11-bach-crab-canon.notes")
    rev_theme = theme2.transposition(-12).retrograde()

    midi = Midi(2, tempo=120)
    midi.seq_notes(theme2)
    midi.seq_notes(rev_theme, track=1)
    midi.write("exercise11-bach-crab-canon.mid")

crab_canon()
