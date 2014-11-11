#!/usr/bin/env python

# Exercise 13.
# Write a Python function
# that filters all three-note chords from the 220 combinations
# and returns only the ones that are not related by transposition.

from itertools import combinations

# initialize the list of all three-note chords
# using the expression provided in the book
all_three_note_chords = list(combinations(range(0, 12), 3))

assert len(all_three_note_chords) == 220,     "220 three-note chords expected"

# among all distinct sets of 3 notes, sorted in increasing values
# keep only the minimum sets, which
# - start with 0
# - list notes in increasing values of intervals
def keep_minimum_sets(sets):
  result=[]
  for notes in sets:
    if notes[0] == 0 \
    and notes[1]-notes[0] <= notes[2]-notes[1] \
    and notes[2]-notes[1] <= 12-notes[2]:
      result.append(notes)
  return result

unrelated_sets_by_transposition_and_inversion = \
  keep_minimum_sets(all_three_note_chords)

print "%s sets found unrelated by transposition and inversion" \
      % len(unrelated_sets_by_transposition_and_inversion)
print unrelated_sets_by_transposition_and_inversion
assert len(unrelated_sets_by_transposition_and_inversion) == 12,  \
                    "12 sets unrelated by transposition and insertion expected"
