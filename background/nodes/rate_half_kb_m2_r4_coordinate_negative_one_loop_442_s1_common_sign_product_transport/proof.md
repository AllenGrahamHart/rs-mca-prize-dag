# Proof

Fix a common sign row and one cubic factor `g_j`.  Reduce the exact common
generators together with `g_j(b)` in lexicographic order.  The resulting
component homomorphism sends the rank-six basis

```text
1,b,b^2,r,br,t
```

into `K_j`.  Reconstruct `c` and then `m` using the two unit denominators
from the mate-coordinate compiler.  Exact reduction in all eight
row/component pairs gives `(KB41T-1)`.

The binary-sextic action is constructed from `(KB41T-2)` and
`Delta=Alpha^2+Beta Gamma`; hence it is row-independent after projection.
For each of the eight rational forced-record `S1` cells, inspection of the
compiled residual factors shows that their only common coefficients are
polynomials in `b,c,m`.  The two forced-loop cells use the same coefficients
and one adjoined element satisfying `theta^2=-m`.  Exact Euler tests show
that `-m` is nonsquare in both `K_j`, so these are the same two quadratic
field extensions for every row.

It follows that each of the ten product ideals is carried coefficient for
coefficient to its representative-row ideal.  The preceding forced-record
nodes prove those ideals empty: six are raw unit ideals, four forced-EF
cells are empty after the nonzero-coordinate guard, and the two loop ideals
are raw unit ideals.  Therefore all ten cells transport to each of the
other three rows.  The outside-sign classifier counts ten `S1` cells per
row, so all forty are deleted.  QED.
