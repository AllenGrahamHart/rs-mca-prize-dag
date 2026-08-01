# Proof

Quotienting by the six-dimensional row span of `B` turns the four nonloop
sum rows into four vectors in the two-dimensional space `V`.  The full
common matrix has rank at most seven if and only if those four vectors span
a space of dimension at most one.

If all four vectors vanish, branch `Z` holds.  Otherwise choose a nonzero
`q_i`.  Four vectors span at most one dimension exactly when every other
`q_j` is proportional to `q_i`.  In dimension two this is equivalent to the
three pair determinants `q_i wedge q_j` vanishing.  Lifting back through the
rank-six base identifies `q_i wedge q_j`, up to a fixed nonzero scalar, with
`det(B,Q_i,Q_j)`.  Enumerating `j!=i` gives the four triples in `(KBPCR-3)`.
QED.
