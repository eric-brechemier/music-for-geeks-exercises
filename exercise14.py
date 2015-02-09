#!/usr/bin/env python

# Exercise 14.
# The method harmonize stacks notes by a fixed interval
# (by thirds, fourths, etc.).
# Create a new version that accepts and uses a
# "chord template" to harmonize a scale.

# Import pyknon from the git submodule in a subdirectory
import sys
sys.path.append('./pyknon')
from pyknon.music import Note, NoteSeq

class Note(Note):
    pass

class NoteSeq(NoteSeq):
    pass

c = Note("C")
assert str(c) == '<C>'
c_major_scale = NoteSeq("C D E F G A B")
assert str(c_major_scale) == '<Seq: [<C>, <D>, <E>, <F>, <G>, <A>, <B>]>'

assert str(c.harmonize(c_major_scale)) == '[<C>, <E>, <G>]'

assert str(c_major_scale.harmonize()) == '[' \
        '<Seq: [<C>, <E>, <G>]>, ' \
        '<Seq: [<D>, <F>, <A>]>, ' \
        '<Seq: [<E>, <G>, <B>]>, ' \
        '<Seq: [<F>, <A>, <C>]>, ' \
        '<Seq: [<G>, <B>, <D>]>, ' \
        '<Seq: [<A>, <C>, <E>]>, ' \
        '<Seq: [<B>, <D>, <F>]>' \
    ']'

assert str(c_major_scale.harmonize(size=4)) == '[' \
        '<Seq: [<C>, <E>, <G>, <B>]>, ' \
        '<Seq: [<D>, <F>, <A>, <C>]>, ' \
        '<Seq: [<E>, <G>, <B>, <D>]>, ' \
        '<Seq: [<F>, <A>, <C>, <E>]>, ' \
        '<Seq: [<G>, <B>, <D>, <F>]>, ' \
        '<Seq: [<A>, <C>, <E>, <G>]>, ' \
        '<Seq: [<B>, <D>, <F>, <A>]>' \
    ']'

assert str(c_major_scale.harmonize(interval=4, size=4)) == '[' \
        '<Seq: [<C>, <F>, <B>, <E>]>, ' \
        '<Seq: [<D>, <G>, <C>, <F>]>, ' \
        '<Seq: [<E>, <A>, <D>, <G>]>, ' \
        '<Seq: [<F>, <B>, <E>, <A>]>, ' \
        '<Seq: [<G>, <C>, <F>, <B>]>, ' \
        '<Seq: [<A>, <D>, <G>, <C>]>, ' \
        '<Seq: [<B>, <E>, <A>, <D>]>' \
    ']'

