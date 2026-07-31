# Proof

After forcing `sigma df=m`, the unforced products are

```text
cd, -cd, -e^2, -m, sigma*me/d, -sigma*me/d.
```

Their factors give the rational residual sextic.  Multiplication by `d^2`
replaces its final rational quadratic by `d^2X^2-m^2e^2Z^2`, proving
`(KB41S2D-1)`.  This scaling is reversible on `d!=0` and commutes with the
binary action.

Apply `E_0,E_1,E_2`.  Sparse cubic-field arithmetic gives seven monomials
per equation.  In each irreducible cubic component, exact grevlex
Buchberger reduction completes after 28 S-pairs.  Its one-term monic basis
elements at exponents `(2,0)` and `(0,2)` are exactly `d^2` and `e^2`.
Therefore the ideal plus the outside guard `d!=0` is empty.

Formula `(KB41S2D-1)` depends on the common row only through `b,c,m` and the
product involution.  Their exact component data are row-independent, so the
guarded deletion applies to all four rows.  QED.
