#!/usr/bin/python

# Exercise 1.
# Extend the function name_to_number
# to deal with notes with mixed flats and sharps

def mod12(n):
  return n % 12

def note_name(number):
  notes = "C C# D D# E F F# G G# A A# B".split()
  return notes[mod12(number)]

def assert_note_has_name(number,name):
  actualName = note_name(number)
  assert actualName  == name, \
    "%(name)s expected for note %(number)d, found %(actual)s" \
      % {"name": name, "number": number, "actual": actualName}

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
  notes = "C . D . E F . G . A . B".split()
  name = note_string[0:1].upper()
  number = notes.index(name)
  acc = accidentals(note_string)
  return mod12(number + acc)

def assert_name_is_note(name,number):
  actualNumber = name_to_number(name)
  assert actualNumber  == number, \
    "Note %(number)d expected for %(name)s, found %(actual)d" \
      % {"number": number, "name": name, "actual": actualNumber}

assert_name_is_note("C#",1)
assert_name_is_note("Db",1)
assert_name_is_note("Ebb",2)
assert_name_is_note("B#",0)

print "OK"

