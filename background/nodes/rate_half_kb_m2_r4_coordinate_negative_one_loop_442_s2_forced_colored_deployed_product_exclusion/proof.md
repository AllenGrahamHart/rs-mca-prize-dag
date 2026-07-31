# Proof

In `S2`, the colored pair `CD` has multiplicity two, so its records are
`cd` and `-cd`.  Representative sign changes exchange them.  Force
`sigma cd=m`.  Then `d=sigma m/c`, the other colored record equals `-m`,
the loop record is `-e^2`, and the two full internal pairs are
`{df,-df}` and `{ef,-ef}`.  Multiplying the six factors `X-uZ` gives
`(KB41S2C-1)`.

Apply the three independent coefficient equations from the binary-sextic
compiler.  Direct sparse arithmetic gives seven `(e,f)` monomials in each.
In each irreducible cubic component, exact grevlex Buchberger reduction
reaches `1` after seven S-pairs.  Thus the representative forced-colored
cell is empty without a guard saturation.

The common-sign transport node proves that the projected `b,c,m` values and
therefore the product involution are coefficient-identical in all four
rows.  Formula `(KB41S2C-1)` uses no other common-row data, and its forced
sign has already disappeared.  Hence the unit certificate transports to
the other three rows.  QED.
