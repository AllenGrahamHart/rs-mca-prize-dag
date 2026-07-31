# Proof

For the chosen `S1` signs, the seven outside products are

```text
ce, -cf, -de, df, -d^2, ef, -ef.
```

The forced record is `-de=m`.  Substituting `e=-m/d` and `f=sd`, removing
the forced product, and writing one factor `X-uZ` for every residual product
gives `(KB41DX-1)`.  Scaling by `d` preserves the homogeneous eigenvalue
equations because `d!=0` for a target representative.

The uniform-row selector says product invariance is equivalent to
`E_0=E_1=E_2=0`.  Sparse multiplication in the six-coordinate common
quotient gives 25 `(d,s)` terms in each equation, avoiding expansion in the
common variables.

Modulo `p=2130706433`, direct multiplication verifies that the two cubics in
`(KB41DX-2)` multiply to the live sextic `S(b)`, and irreducibility testing
proves that both quotients are fields.  In each field the relation

```text
(b^2+(i-1)b+1)r=-(b^2-(i+1)b+1)
```

has nonzero coefficient, so `r` and then `t=-i/r` lie in the cubic field.
Substitution replays all six printed common quotient relations.  Since the
two components have total dimension six, they exhaust the rank-six common
quotient.

Run Buchberger reduction over each cubic field with grevlex order in
`(d,s)`.  Both computations start from three 25-term polynomials with leading
monomial `d^6s^4`.  In each component the same exact sequence reaches a
constant after 79 S-pairs.  Monic normalization makes that constant `1`.
Thus both component ideals, and hence their product-algebra ideal, are the
unit ideal.  There is no product-invariant forced-`DE` realization. QED.
