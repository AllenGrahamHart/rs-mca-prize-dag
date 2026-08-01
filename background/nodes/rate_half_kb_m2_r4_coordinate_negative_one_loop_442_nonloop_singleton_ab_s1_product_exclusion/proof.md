# Proof

The `S1` products are

```text
{alpha c e, beta c f, -d^2, gamma d e, delta d f, +/-e f},
```

with parity `alpha beta gamma delta`.  The outside sign action gives ten
forced-record cells: two internal, two colored, four `EF`, and two loop
parities.

For the eight rational cells, set the forced record equal to the parent
mate and eliminate its determined outside representative.  The three
independent binary-sextic invariance equations then have the sparse
profiles in `(KB41BS1-1)`.  Exact Buchberger reduction produces raw units
for internal and colored cells.  Every forced-`EF` basis contains the
monic equation `s=0`, contradicting its nonzero representative guard.

For a forced loop, `-d^2=m`.  The two identities in `(KB41BS1-2)`
provide a base-field choice `d=theta` in each `b` row.  The residual
sextic has factors

```text
(X+c e Z)(X+c f Z)(X+theta e Z)
(X-delta theta f Z)(X^2-e^2f^2Z^2).
```

Its three 17-term invariance equations are raw unit ideals after 55 or 57
S-pairs according to parity.  Changing the sign of `theta` is an outside
`D` sign change and does not create another cell.

Under `c -> -c`, simultaneously change the signs of `E,F`.  The colored
products and full `EF` pair are preserved, `DE,DF` both change sign,
and their two sign changes preserve the four-sign parity.  Thus the checked
positive-`c` representatives cover the opposite sign.  Both `b` roots
were replayed independently.

This deletes all ten `S1` cells.  The parent nodes already delete all six
`S0` and four `S2` cells, exhausting the twenty-cell forced-record
census.  No outside product multiset remains, so later q and interpolation
conditions are vacuous for this common orbit. QED.
