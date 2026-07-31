# Proof

The `S0` products are

```text
{alpha c e, beta c f, +/-d e, +/-d f, gamma e f},
```

with parity `alpha beta gamma`.  The outside sign action reduces the
forced record to colored, `EF`, or internal, with two parity values in
each type.  Set that record equal to the forced mate and construct the
residual sextic `F(X,Z)`.

As in the parent `S2` proof, three coefficient equations of

```text
F(Alpha X+Beta Z,Gamma X-Alpha Z)
 =(Alpha^2+Beta Gamma)^3 F(X,Z)
```

are necessary and sufficient for the six roots to form three product-
involution pairs.  After forced-record substitution these are sparse
polynomials in two outside representatives.

Exact two-variable Buchberger reduction gives `(KB41BS0-1)` in both
`b` rows and both parities.  The colored cell is a raw unit ideal.  The
forced-`EF` basis contains the square of the remaining representative;
the forced-internal basis contains that representative itself.  Its
nonzero guard deletes both cells.

Under `c -> -c`, change both colored outside representative signs.  The
colored products and both full internal signed pairs are merely permuted,
the `EF` product is unchanged, and the two sign changes preserve
`alpha beta gamma`.  Hence the checked positive-`c` systems cover the
opposite sign.  The two `b` rows cover the parent finite atlas. QED.
