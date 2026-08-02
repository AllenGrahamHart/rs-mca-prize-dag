# Proof

Every map `X -> aX` or `X -> a/X` commutes with `X -> -X`.  Pulling back a
positive form by such a map, and multiplying by `X^4` in the reciprocal
case, preserves

```text
H=A_2(X^2)T^2+A_0(X^2)+XT B_1(X^2)
```

and its degree bounds.  Evaluating the pulled-back form at the transformed
source point gives a nonzero scalar multiple of the old target quadratic.
Thus target products and sums are unchanged, while source quotient labels,
pairings, and guards transport bijectively.  The complete Vieta equations
therefore transport as well.

The common compiler orders every cell `3,...,14` with `LC` first in its
first complete pair.  Pullback by `X -> -X` sends

```text
(1,epsilon_1 i;r,epsilon_2 i r;t)
 -> (-1,-epsilon_1 i;-r,-epsilon_2 i r;-t).
```

The first root is the loop lift, so replacing `-1` by its canonical deck
mate `1` changes no loop record.  This is the first action in `(KBRSQ-1)`.
The reciprocal calculation in the complete cell-5/8 theorem gives the
second action.  They generate all four sign rows independently.

Cell `0` has singleton `LC` and first pair `AB+1,AB+2`.  Transpose those
identical roles, then scale by `1/(epsilon_1 i)`.  The first pair becomes
`(1,-epsilon_1 i)`, while the second pair retains relative sign
`epsilon_2`; hence only `epsilon_1` flips.  Pullback by `X -> 1/X` fixes the
first root and sends both relative signs to their negatives.  These two
actions generate all four rows.

Cell `1` has pairs `(AB+1,AB-)`, `(AB+2,AC)` and cell `2` has
`(AB+1,AC)`, `(AB+2,AB-)`.  Reciprocity `X -> 1/X` flips both signs in a
fixed cell.  Transpose the `AB+` roles and rescale by `1/r`; this exchanges
cells `1,2` and sends `(epsilon_1,epsilon_2)` to
`(epsilon_2,epsilon_1)`.  The product of the signs is invariant and is the
only invariant, giving exactly two orbits among these eight rows.

The duplicate-role compiler proves `(KBRSQ-2)`.  Seven of its cell orbits
lie in `3,...,14`, one is cell `0`, and one is `[1,2]`.  Their representative
counts are therefore `7+1+2=10`.  The exact enumerator independently obtains
five orbits of size eight and five of size four, totaling 60.  The complete
cell-5/8 theorem deletes exactly the `[5,8]` orbit, leaving nine. QED.
