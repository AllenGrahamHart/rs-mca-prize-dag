# Proof

Relative to the preceding forced-`DE` cell, only the `CE` singleton sign
changes.  Since `e=-m/d`, its product changes from `-cm/d` to `+cm/d`, so
the first residual factor changes from `dX+cmZ` to `dX-cmZ`.  This gives
`(KB41DO-1)`; every other factor and the common quotient are unchanged.

Rebuild the three uniform coefficient equations by sparse quotient
multiplication.  Each has 25 outside monomials.  Project to the same two
irreducible cubic common components and replay all six common quotient
relations.  Exact grevlex Buchberger reduction over each cubic field reaches
a nonzero constant after 79 S-pairs, normalized to `1`.  Hence the raw ideal
is the unit ideal in both components and the cell is empty. QED.
