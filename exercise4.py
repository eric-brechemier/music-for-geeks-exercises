#!/usr/bin/env python
#
# Exercise 4.
# Extend the function get_quality to deal with doubly augmented and
# doubly diminished intervals such as Eb-F## and E-Cbb

def mod12(n):
    return n % 12

def accidentals(note_string):
    acc = len(note_string[1:])
    if "#" in note_string:
        return acc
    elif "b" in note_string:
        return -acc
    else:
        return 0

def name_to_number(note_string):
    notes = "C . D . E F . G . A . B".split()
    name = note_string[0:1].upper()
    number = notes.index(name)
    acc = accidentals(note_string)
    return mod12(number + acc)

def assert_name_is_note(name,number):
    actual_number = name_to_number(name)
    assert actual_number == number, (
        "Note %(number)d expected for %(name)s, found %(actual)d" %
        {"number": number, "name": name, "actual": actual_number}
    )

assert_name_is_note("C#",1)
assert_name_is_note("Db",1)
assert_name_is_note("Ebb",2)
assert_name_is_note("B#",0)

# interval from note y to note x (sic)
def interval(x, y):
    return mod12(x - y)

def assert_interval_is(from_note, to_note, interval_value):
    actual_interval_value = interval(to_note, from_note)
    assert actual_interval_value == interval_value, (
        "Interval %(interval)s expected for %(from_note)d-%(to_note)d, "
        "found: %(actual_interval)s" %
        {
            "interval": interval_value,
            "actual_interval": actual_interval_value,
            "from_note": from_note,
            "to_note": to_note
        }
    )

assert_interval_is(2, 4, 2)
assert_interval_is(4, 2, 10)

def name_to_diatonic(note_string):
    notes = "C D E F G A B".split()
    name = note_string[0:1].upper()
    return notes.index(name)

def assert_name_is_diatonic(name,number):
    actual_number = name_to_diatonic(name)
    assert actual_number == number, (
        "Diatonic %(number)d expected for %(name)s, found %(actual)d" %
        {"number": number, "name": name, "actual": actual_number}
    )

assert_name_is_diatonic("C",0)
assert_name_is_diatonic("C#",0)
assert_name_is_diatonic("Db",1)
assert_name_is_diatonic("D",1)

class SimpleMusicError(Exception):
    pass

def get_quality(diatonic_interval, chromatic_interval):
    if diatonic_interval in [0, 3, 4]:
        quality_map = ["Diminished", "Perfect", "Augmented"]
    else:
        quality_map = ['Diminished', 'Minor', 'Major', 'Augmented']

    index_map = [-1, 0, 2, 4, 6, 7, 9]
    try:
        return quality_map[chromatic_interval - index_map[diatonic_interval]]
    except IndexError:
        raise SimpleMusicError("Sorry, I can't deal with this interval :-(")

def interval_name(note1, note2):
    quantities = [
        "Unison", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh"
    ]
    n1, n2 = name_to_number(note1), name_to_number(note2)
    d1, d2 = name_to_diatonic(note1), name_to_diatonic(note2)
    chromatic_interval = interval(n2, n1)
    diatonic_interval = (d2 - d1) % 7
    quantity_name = quantities[diatonic_interval]
    quality_name = get_quality(diatonic_interval, chromatic_interval)
    return "%s %s" % (quality_name, quantity_name)

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
