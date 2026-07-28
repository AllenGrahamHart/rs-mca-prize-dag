# Proof

The exact profile/parity reduction proves that every pair-feasible
folded-profile `(3,4,0)` vector at `V=60` has one of the eight profiles printed
in the statement.

The quotient exclusion removes `(0,3,2)`, `(6,2,0,1)`, and `(3,0,3)`. The
two-odd exclusion removes `(2,7)` and `(1,5,1)`. The three individual profile
nodes remove `(4,2,2)`, `(5,4,1)`, and `(6,6)`. These sets are disjoint and
their union is the exact eight-profile reduction, so `V=60` is impossible.

The preceding endpoint theorem left only positive even `V<=60`. Removing
`V=60` advances the live frontier to positive even `V<=58`. QED.
