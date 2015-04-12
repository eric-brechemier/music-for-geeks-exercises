; Based on 'Toot 1: Play One Note' and 'Toot 2: P-Fields'
; From: http://www.csounds.com/toots/index.html

; header
sr = 44100
kr = 4410
ksmps = 10
nchnls = 1

; instruments

; Instrument 1
; with parameters:
;   * p1: (reserved) instrument number
;   * p2: (reserved) start time
;   * p3: (reserved) duration
;   * p4: amplitude
;   * p5: frequency

instr 1
  a1 oscil p4, p5, 1
  out a1
endin
