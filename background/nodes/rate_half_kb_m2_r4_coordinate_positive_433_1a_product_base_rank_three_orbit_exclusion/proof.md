# Proof

If `rank P<5`, all six maximal minors vanish.

For cell 11, `(KBPBR-2)` is nonzero because every displayed factor is an
admissibility guard.  Hence `D_1!=0`, a contradiction.

For cell 0, `D_1=0` first forces `b=-c^2`.  Exact polynomial division of
the specialized `D_0` gives `(KBPBR-3)`, again a product of nonzero guards.
Thus cell 0 cannot have product rank below five.

For cell 14, `D_1=0` forces `b=c^2`.  The remaining minor equations include
`E_2=E_5=0` from `(KBPBR-4)`.  Their displayed linear combination is
`-(c^2-1)(r^4-1)`.  Target distinctness gives `c^2!=1`; source-label
distinctness gives `r^2!=+/-1`, hence `r^4!=1`.  This is a contradiction.

Finally, the loop sum row has entries `(0,...,0,lambda,lambda^2)` in the
last two coefficient columns, with `lambda!=0`, whereas every product row
vanishes in those columns.  It is independent of `P`, so `rank B=6`. QED.
