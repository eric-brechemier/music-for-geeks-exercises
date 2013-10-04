#!/usr/bin/env python

# Exercise 5.
# Read page 77 in (Hewlett, 1992) or read [1] and implement a
# function to return the interval name using his numerical system.
#
# [1] See Example 3 in
# A Base-40 Number-line Representation of Musical Pitch Notation
# by Walter B. Hewlett
# http://www.ccarh.org/publications/reprints/base40/

def mod12(n):
    return n % 12

def note_name(number):
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    return notes[mod12(number)]

def assert_note_has_name(number,name):
    actual_name = note_name(number)
    assert actual_name == name, (
        "%(name)s expected for note %(number)d, found %(actual)s" %
        {"name": name, "number": number, "actual": actual_name}
    )

assert_note_has_name(0,"C")
assert_note_has_name(1,"C#")
assert_note_has_name(13,"C#")
assert_note_has_name(3,"D#")

def accidentals(note_string):
    acc = len(note_string[1:])
    if "#" in note_string:
        return acc
    elif "b" in note_string:
        return -acc
    else:
        return 0

def name_to_number(note_string):
    notes = [
        "Cbb", "Cb", "C", "C#", "C##", ".",
        "Dbb", "Db", "D", "D#", "D##", ".",
        "Ebb", "Eb", "E", "E#", "E##",
        "Fbb", "Fb", "F", "F#", "F##", ".",
        "Gbb", "Gb", "G", "G#", "G##", ".",
        "Abb", "Ab", "A", "A#", "A##", ".",
        "Bbb", "Bb", "B", "B#", "B##"
    ]
    return 1 + notes.index( note_string )

def assert_name_is_note(name,number):
    actual_number = name_to_number(name)
    assert actual_number == number, (
        "Note %(number)d expected for %(name)s, found %(actual)d" %
        {"number": number, "name": name, "actual": actual_number}
    )

# Test each of the value in use in Hewlett's base-40 system [1]
assert_name_is_note("Cbb",  1)
assert_name_is_note("Cb",   2)
assert_name_is_note("C",    3)
assert_name_is_note("C#",   4)
assert_name_is_note("C##",  5)
# -
assert_name_is_note("Dbb",  7)
assert_name_is_note("Db",   8)
assert_name_is_note("D",    9)
assert_name_is_note("D#",  10)
assert_name_is_note("D##", 11)
# -
assert_name_is_note("Ebb", 13)
assert_name_is_note("Eb",  14)
assert_name_is_note("E",   15)
assert_name_is_note("E#",  16)
assert_name_is_note("E##", 17)
assert_name_is_note("Fbb", 18)
assert_name_is_note("Fb",  19)
assert_name_is_note("F",   20)
assert_name_is_note("F#",  21)
assert_name_is_note("F##", 22)
# -
assert_name_is_note("Gbb", 24)
assert_name_is_note("Gb",  25)
assert_name_is_note("G",   26)
assert_name_is_note("G#",  27)
assert_name_is_note("G##", 28)
# -
assert_name_is_note("Abb", 30)
assert_name_is_note("Ab",  31)
assert_name_is_note("A",   32)
assert_name_is_note("A#",  33)
assert_name_is_note("A##", 34)
# -
assert_name_is_note("Bbb", 36)
assert_name_is_note("Bb",  37)
assert_name_is_note("B",   38)
assert_name_is_note("B#",  39)
assert_name_is_note("B##", 40)

def interval_name(note1, note2):
    # from 'Computation of Intervals' in [1],
    # completed with doubly augmented interval names
    INTERVAL_NAMES = [
      'Perfect Unison', #0
      'Augmented Unison', #1
      'Doubly Augmented Unison', #2
      'Doubly Diminished Second', #3
      'Diminished Second', #4
      'Minor Second', #5
      'Major Second', #6
      'Augmented Second', #7
      'Doubly Augmented Second', #8
      'Doubly Diminished Third', #9
      'Diminished Third', #10
      'Minor Third', #11
      'Major Third', #12
      'Augmented Third', #13
      'Doubly Augmented Third', #14
      'Doubly Diminished Fourth', #15
      'Diminished Fourth', #16
      'Perfect Fourth', #17
      'Augmented Fourth', #18
      'Doubly Augmented Fourth', #19
      '-', #20
      'Doubly Diminished Fifth', #21
      'Diminished Fifth', #22
      'Perfect Fifth', #23
      'Augmented Fifth', #24
      'Doubly Augmented Fifth', #25
      'Doubly Diminished Sixth', #26
      'Diminished Sixth', #27
      'Minor Sixth', #28
      'Major Sixth', #29
      'Augmented Sixth', #30
      'Doubly Augmented Sixth', #31
      'Doubly Diminished Seventh', #32
      'Diminished Seventh', #33
      'Minor Seventh', #34
      'Major Seventh', #35
      'Augmented Seventh', #36
      'Doubly Augmented Seventh', #37
      'Doubly Diminished Octave', #38
      'Diminished Octave', #39
      'Perfect Octave' #40 (unused: displayed as 'Perfect Unison')
    ]

    delta = (name_to_number(note2) - name_to_number(note1)) % 40;
    return INTERVAL_NAMES[delta]

def assert_interval_name_is(note1, note2, name):
    actual_name = interval_name(note1, note2)
    assert actual_name == name, (
        "Interval %(interval)s expected for %(note1)s-%(note2)s, "
        "found: %(actual)s" %
        {
            "interval": name, "actual": actual_name,
            "note1": note1, "note2": note2
        }
    )

assert_interval_name_is("C", "C", "Perfect Unison")
assert_interval_name_is("C", "Db", "Minor Second")
assert_interval_name_is("C", "D", "Major Second")
assert_interval_name_is("C", "Eb", "Minor Third")
assert_interval_name_is("C", "E", "Major Third")
assert_interval_name_is("C", "F", "Perfect Fourth")
assert_interval_name_is("C", "F#", "Augmented Fourth")
assert_interval_name_is("C", "Gb", "Diminished Fifth")
assert_interval_name_is("C", "G", "Perfect Fifth")
assert_interval_name_is("C", "Ab", "Minor Sixth")
assert_interval_name_is("C", "A", "Major Sixth")
assert_interval_name_is("C", "Bb", "Minor Seventh")
assert_interval_name_is("C", "B", "Major Seventh")

assert_interval_name_is("Eb", "C#", "Augmented Sixth")
assert_interval_name_is("Eb", "F#", "Augmented Second")
assert_interval_name_is("E", "Cb", "Diminished Sixth")

assert_interval_name_is("Eb", "F##", "Doubly Augmented Second")
assert_interval_name_is("E", "Cbb", "Doubly Diminished Sixth")

print "OK"
