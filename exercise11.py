#!/usr/bin/env python

# Exercise 11.
# Create your own crab canon using the function crab_canon.

# Import pyknon from the git submodule in a subdirectory
import sys
sys.path.append('./pyknon')
from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq

# filename - file name, without extension
#            The same file name is used as input, with extension .notes,
#            to read the list of notes for the theme,
#            and as output, with the extension .mid,
#            to generate corresponding MIDI file.
def crab_canon(filename):
    theme2 = NoteSeq("file://%s.notes" % filename)
    rev_theme = theme2.transposition(-12).retrograde()

    midi = Midi(2, tempo=120)
    midi.seq_notes(theme2)
    midi.seq_notes(rev_theme, track=1)
    midi.write("%s.mid" % filename)

crab_canon("exercise11-bach-crab-canon")
