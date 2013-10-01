#!/usr/bin/env python
#
# Exercise 3.
# Create a function music_duration to claculate the total duration
# in minutes of a composition. This function accepts four parameters:
#   - the time signature as a string,
#   - the number of bars,
#   - the reciprocal of the note value of the tempo
#     (for example, use 4 if the note value is a quarter),
#   - and the tempo itself.
# It assumes that the tempo and time signature of a composition won't change.

from __future__ import division

def note_duration(note_value, unity, tempo):
  return (60.0 * note_value) / (tempo * unity)

def assert_note_duration_is(note_value, duration):
  UNITY = 1/4
  TEMPO = 90
  ACCURACY = 1/100
  actualDuration = note_duration(note_value, UNITY, TEMPO)
  assert \
    abs( actualDuration - duration ) < ACCURACY, \
    "%(duration).2f seconds expected for note value %(note_value)s" \
    % {"duration": actualDuration, "note_value": note_value}

assert_note_duration_is(1/4, 0.66)
assert_note_duration_is(1/2, 1.33)
assert_note_duration_is(1/8, 0.33)

def music_duration(time_signature, bars, reciprocal_note_value, tempo):
  return None

assert music_duration("4/4", 10, 4, 60) == 40 / 60, \
  "duration of 40 quarter notes with 60 quarter notes per minute expected, " \
  "found: %s minutes" % music_duration("4/4", 10, 4, 60)
