# Proof

In `S2`, forcing `EE=-e^2=m` leaves the three full signed product pairs

```text
{cd,-cd}, {df,-df}, {ef,-ef}.
```

Their factors are the three quadratics in `(KB41S2L-1)`.  Since
`e^2=-m`, the last is `X^2+m f^2Z^2`; neither a square root nor a tower
field appears.

Apply `E_0,E_1,E_2`.  Sparse cubic-field arithmetic gives seven `(d,f)`
monomials in each equation.  In each irreducible cubic component, exact
grevlex Buchberger reduction reaches `1` after seven S-pairs.  Thus the
representative forced-loop cell is empty without guard saturation.

Formula `(KB41S2L-1)` depends on the common row only through `b,c,m` and the
product involution.  Their exact component data are row-independent, so the
raw unit certificate applies to all four rows.  The forced-cell classifier
has exactly four `S2` cells per row; the preceding three nodes delete the
other three.  Hence the complete `S2` product frontier is empty.  QED.
