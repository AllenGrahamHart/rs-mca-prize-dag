# Proof

After forcing `tau_0 ef=m`, the unforced products are

```text
ce, tau_0*cm/e, de, -de, tau_0*dm/e, -tau_0*dm/e.
```

Their factors give the rational residual sextic.  Multiplication by `e^3`
clears one linear and one quadratic denominator and gives `(KB41S0E-1)`.
This scaling is reversible on `e!=0` and commutes with the action on
`(X,Z)`.

For each parity, apply `E_0,E_1,E_2`.  Sparse cubic-field arithmetic gives
twelve monomials per equation.  In each cubic component, exact grevlex
Buchberger reduction completes after 190 S-pairs.  The one-term monic basis
element at exponent `(0,2)` is `e^2`, so the ideal plus `e!=0` is empty.

The residual form depends on the common row only through `b,c,m` and the
product involution.  Their component data are row-independent, so both
parity deletions apply to all four rows.  QED.
