#!/usr/bin/env python

# Exercise 13.
# Write a Python function
# that filters all three-note chords from the 220 combinations
# and returns only the ones that are not related by transposition.

from itertools import combinations

# initialize the list of all three-note chords
# using the expression provided in the book
all_three_note_chords = list(combinations(range(0, 12), 3))

print "%s total distinct sets of three notes:" \
      % len(all_three_note_chords)
print all_three_note_chords

assert len(all_three_note_chords) == 220,     "220 three-note chords expected"

# among all distinct sets of 3 notes, sorted in increasing values
# keep only the minimum sets, which
# 1) have value 0 for the first note
# 2) do not match a lower set by shifting the set
#   to bring the second or the third note down to 0
#
# The first condition restricts the selection
# to sets of the form {0,a,b} with a < b.
#
# The second condition requires to compare {0,a,b}
# with the sets {12-a,a-a,b-a} and {12-b,12+a-b,b-b}.
# Since 0 < a < b < 12, we have:
#   * 0 < b-a
#   * b-a < 12-a
#   * 12-b < 12-b+a
#
# Thus, the two extra sets can be written as:
# {0,b-a,12-a} and {0,12-b,12+a-b}
# listing items in increasing order.
#
# The set {0,a,b} is lower than both {0,b-a,12-a} and {0,12-b,12+a-b}
# in lexical order if and only if:
#   * a < b-a  or ( a == b-a  and b <= 12-a   ),
# and
#   * a < 12-b or ( a == 12-b and b <= 12+a-b ).
def keep_minimum_sets(sets):
    result=[]
    for notes in sets:
        if notes[0] != 0:
            continue
        a = notes[1]
        b = notes[2]
        if  ( a < b-a  or ( a == b-a  and b <= 12-a   ) ) \
        and ( a < 12-b or ( a == 12-b and b <= 12+a-b ) ):
            result.append(notes)
    return result

unrelated_sets_by_transposition = \
  keep_minimum_sets(all_three_note_chords)

print "%s sets found unrelated by transposition:" \
      % len(unrelated_sets_by_transposition)
print unrelated_sets_by_transposition
assert len(unrelated_sets_by_transposition) == 19,  \
                                 "19 sets unrelated by transposition expected"
