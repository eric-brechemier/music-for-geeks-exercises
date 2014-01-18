#!/usr/bin/env python

# Exercise 12.
# Change the canon function to have a different process.
# Instead of inversion, use transposition, retrograde,
# or other operations and see how it sounds.

# Import pyknon from the git submodule in a subdirectory
import sys
sys.path.append('./pyknon')
from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq

def canon():
    theme = NoteSeq("file://exercise12-bach-canon-quaerendo-invenietis.notes")
    part1 = theme + theme[2:] + theme[2:11]
    part2 = theme + theme[2:] + theme[2:4]

    voice1 = part1
    voice2 = part2.inversion_startswith(Note(2, 4))

    midi = Midi(2, tempo=150)
    midi.seq_notes(voice1, time=3, track=0)
    midi.seq_notes(voice2, time=13, track=1)
    midi.write("exercise12-canon-by-inversion.mid")

canon()
