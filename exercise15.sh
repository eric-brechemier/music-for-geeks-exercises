#!/bin/sh
# Requires csound (5.17)

# Exercise 15.
# Try to construct a scale using only frequencies from the harmonic series.
# Notice how it sounds different from the equal temperament.

echo 'Generate WAV file from Orchestra and Score files using CSound'

if test -z "$( which csound )"
then
  echo 'Csound is required.'
  echo 'You can download it from: https://csound.com'
  exit 1
fi
csound \
  -g \
  -W -o exercise15-harmonic-series.wav \
  exercise15-csound.orc \
  exercise15-csound.sco \
  || exit 2

echo 'Done.'
