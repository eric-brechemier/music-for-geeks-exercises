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

def note_harmonize_template(self, scale, indices):
    # TODO: implement
    # Hint: modify previous implementation of Note.harmonize()
    return

def note_harmonize(self, scale, interval=3, size=3):
    # TODO: implement using harmonize_template()
    return

Note.harmonize_template = note_harmonize_template
Note.harmonize = note_harmonize

def noteseq_harmonize_template(self, indices):
    # TODO: implement
    # Hint: modify previous implementation of NoteSeq.harmonize()
    return

NoteSeq.harmonize_template = noteseq_harmonize_template

c = Note("C")
assert str(c) == '<C>'
c_major_scale = NoteSeq("C D E F G A B")
assert str(c_major_scale) == '<Seq: [<C>, <D>, <E>, <F>, <G>, <A>, <B>]>'

assert str(c.harmonize(c_major_scale)) == '[<C>, <E>, <G>]'
assert str(c.harmonize_template(c_major_scale, [1, 3, 5])) == '[<C>, <E>, <G>]'

assert str(c.harmonize_template(c_major_scale, [1, 2, 3])) == '[<C>, <D>, <E>]'
assert str(c.harmonize_template(c_major_scale, [1, 4, 2])) == '[<C>, <F>, <D>]'
assert str(c.harmonize_template(c_major_scale, [5, 7, 9])) == '[<G>, <B>, <D>]'

assert str(c.harmonize_template(c_major_scale, [1, 2, 3, 4])) == \
       '[<C>, <D>, <E>, <F>]'
assert str(c.harmonize_template(c_major_scale, [1, 3, 5, 6, 8])) == \
       '[<C>, <E>, <G>, <A>, <C>]'

assert str(c_major_scale.harmonize()) == '[' \
        '<Seq: [<C>, <E>, <G>]>, ' \
        '<Seq: [<D>, <F>, <A>]>, ' \
        '<Seq: [<E>, <G>, <B>]>, ' \
        '<Seq: [<F>, <A>, <C>]>, ' \
        '<Seq: [<G>, <B>, <D>]>, ' \
        '<Seq: [<A>, <C>, <E>]>, ' \
        '<Seq: [<B>, <D>, <F>]>' \
    ']'
assert str(c_major_scale.harmonize_template([1, 3, 5])) == '[' \
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
assert str(c_major_scale.harmonize_template([1, 3, 5, 7])) == '[' \
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
assert str(c_major_scale.harmonize_template([1, 4, 7, 10])) == '[' \
        '<Seq: [<C>, <F>, <B>, <E>]>, ' \
        '<Seq: [<D>, <G>, <C>, <F>]>, ' \
        '<Seq: [<E>, <A>, <D>, <G>]>, ' \
        '<Seq: [<F>, <B>, <E>, <A>]>, ' \
        '<Seq: [<G>, <C>, <F>, <B>]>, ' \
        '<Seq: [<A>, <D>, <G>, <C>]>, ' \
        '<Seq: [<B>, <E>, <A>, <D>]>' \
    ']'

assert str(c_major_scale.harmonize_template([1, 4, 6])) == '[' \
        '<Seq: [<C>, <F>, <B>]>, ' \
        '<Seq: [<D>, <G>, <C>]>, ' \
        '<Seq: [<E>, <A>, <D>]>, ' \
        '<Seq: [<F>, <B>, <E>]>, ' \
        '<Seq: [<G>, <C>, <F>]>, ' \
        '<Seq: [<A>, <D>, <G>]>, ' \
        '<Seq: [<B>, <E>, <A>]>' \
    ']'

assert str(c_major_scale.harmonize_template([1, 2, 4, 6])) == '[' \
        '<Seq: [<C>, <D>, <F>, <A>]>, ' \
        '<Seq: [<D>, <E>, <G>, <B>]>, ' \
        '<Seq: [<E>, <F>, <A>, <C>]>, ' \
        '<Seq: [<F>, <G>, <B>, <D>]>, ' \
        '<Seq: [<G>, <A>, <C>, <E>]>, ' \
        '<Seq: [<A>, <B>, <D>, <F>]>, ' \
        '<Seq: [<B>, <C>, <E>, <G>]>' \
    ']'

assert str(c_major_scale.harmonize_template([1, 5, 6, 9, 12])) == '[' \
        '<Seq: [<C>, <G>, <A>, <D>]>, ' \
        '<Seq: [<D>, <A>, <B>, <E>]>, ' \
        '<Seq: [<E>, <B>, <C>, <F>]>, ' \
        '<Seq: [<F>, <C>, <D>, <G>]>, ' \
        '<Seq: [<G>, <D>, <E>, <A>]>, ' \
        '<Seq: [<A>, <E>, <F>, <B>]>, ' \
        '<Seq: [<B>, <F>, <G>, <C>]>' \
    ']'

