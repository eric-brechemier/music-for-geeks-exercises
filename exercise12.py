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

def inversion(notes):
    return notes.inversion_startswith(Note("D,"))

def transposition(notes):
    return notes.transposition_startswith(Note("Eb,"))

def retrograde(notes):
    return notes.retrograde()

def rotation(notes):
    return notes.rotate(5)

def repetitionTwiceFaster(notes):
    return notes.stretch_dur(0.5) + notes.stretch_dur(0.5)

# operation - function(notes), function applied to the notes of part2
#             to produce the notes of voice2 for the canon
# operationName - string, name of the operation,
#                 used in file name of generated MIDI
def canon(operation, operationName):
    theme = NoteSeq("file://exercise12-bach-canon-quaerendo-invenietis.notes")
    part1 = theme + theme[2:] + theme[2:11]
    part2 = theme + theme[2:] + theme[2:4]

    voice1 = part1
    voice2 = operation(part2)

    midi = Midi(2, tempo=150)
    midi.seq_notes(voice1, time=3, track=0)
    midi.seq_notes(voice2, time=13, track=1)
    output_file = "exercise12-canon-by-%s.mid" % operationName
    print "Write " + output_file
    midi.write(output_file)

canon(inversion, "inversion")
canon(transposition, "transposition")
canon(retrograde, "retrograde")
canon(rotation, "rotation")
canon(repetitionTwiceFaster, "repetition-twice-faster")

print "Done."
