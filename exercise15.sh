#!/bin/sh
# Requires csound (5.17)

# Exercise 15.
# Try to construct a scale using only frequencies from the harmonic series.
# Notice how it sounds different from the equal temperament.

echo 'Generate WAV file from Orchestra and Score files using CSound'
csound \
  -g \
  -W -o exercise15-harmonic-series.wav \
  exercise15-csound.orc \
  exercise15-csound.sco
