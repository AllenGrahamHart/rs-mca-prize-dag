# Proof

After forcing `sigma ef=m`, the unforced products are

```text
cd, -cd, -e^2, sigma*dm/e, -sigma*dm/e, -m.
```

Their six factors give the residual sextic before scaling.  Multiplication
by `e^2` replaces its rational quadratic factor by
`e^2X^2-m^2d^2Z^2`, proving `(KB41S2E-1)`.  This scaling is reversible on
the required guard `e!=0` and commutes with the action on `(X,Z)`.

Apply `E_0,E_1,E_2`.  Sparse cubic-field arithmetic gives seven monomials
per equation.  In each irreducible cubic component, exact grevlex
Buchberger reduction completes after 28 S-pairs.  The monic reduced element
with leading monomial `e^2` has one term, hence is exactly `e^2`.  Therefore
the ideal plus the outside guard is empty.

Formula `(KB41S2E-1)` depends on the common row only through `b,c,m` and the
product involution.  Their exact component data are row-independent by the
common-sign product transport theorem, so the guarded deletion applies to
all four rows.  QED.
