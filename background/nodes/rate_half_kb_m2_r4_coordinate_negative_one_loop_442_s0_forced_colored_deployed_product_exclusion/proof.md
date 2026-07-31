# Proof

In `S0`, the singleton products are `alpha CE`, `beta CF`, and `gamma EF`,
while `DE` and `DF` occur as full signed pairs.  The sign action has two
orbits indexed by `tau_0=alpha beta gamma`; choose
`alpha=beta=1, gamma=tau_0`.

Force `CE=ce=m`.  The remaining products are

```text
cf, dm/c, -dm/c, df, -df, tau_0*mf/c.
```

Their six factors give `(KB41S0C-1)`.  Apply `E_0,E_1,E_2`.  For each
parity, sparse cubic-field arithmetic gives eleven `(d,f)` monomials per
equation.  In each irreducible cubic component, exact grevlex Buchberger
reduction reaches `1` after 29 S-pairs.  Thus both representative parity
cells are empty without guard saturation.

The residual form depends on the common row only through `b,c,m` and the
product involution.  Their exact component data are row-independent, so
both raw unit certificates apply to all four rows.  The `CE/CF` skeleton
automorphism identifies the two colored singleton choices.  QED.
