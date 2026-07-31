# Proof

With the exact relative `U/V` normalization, the four fixed-moving same
allocation equations are quadratic in `b`. A common root forces all maximal
minors of their `4 x 3` coefficient matrix to vanish and the first-two-row
kernel to lie on the Veronese conic.

## Common components

The three minor projections share, beyond the printed open factors,

```text
L=4p+5t+4
```

and the reciprocal quartic

```text
16p^4+220p^3t-20p^3+579p^2t^2+684p^2t-72p^2
+503pt^3+1218pt^2+684pt-20p
+140t^4+503t^3+579t^2+220t+16.             (1)
```

On `L=0`, exact minor and projection gcds have support only on `w=1`,
`t=0,-1,-4`, or `p=1`, all forbidden.

For `(1)`, take the affine `w`-resultant of residual minor 0 and the residual
kernel conic. It is not divisible by `(1)`. Their `p`-resultant is the
degree-472 polynomial with digest

```text
a04c532e08a8bf9fff2337895559c14e32e4242c51e1be747890e329e40ba6b0.
```

It has 28 irreducible factors. A root of an irreducible degree-`d` factor
lies in `F_(p^6)` only if `d` divides `6`; eight factors are discarded by
this exact field criterion. On every remaining factor, the component and
minor-conic resultant have only linear deployed `p` roots, and all deployed
`w` roots are replayed in all four original equations. The ledger is

```text
20 endpoint candidates;
12 boundary;
4 empty at the minor-conic or original-equation gate;
4 admissible base-field q-slice points, at norm factors 1,2,3,4.
```

## Full quotient rejection

For each printed point reconstruct the positive fixed-moving source form
`H=U+XV` and its norm `G=U^2-WV^2`. The aligned label locators are

```text
J={2,1/2,b,1/b,c,d},
I={w,w^-1,z,z^-1,c^-1,d^-1},
K=I minus {w^-1}.
```

The q-slice resultant first matches
`(W-w)^4((W-c^-1)(W-d^-1))^2`, independently checking reconstruction and
label orientation. Multiplying `(KBQ2-2)` by its source-deck conjugate gives

```text
Res_T(P_J,G) ~ K_5^4 q^2,                 (2)
q^2 Res_T(P_I,G) ~ R_7^4.                 (3)
```

Exact coefficient comparison fails both `(2)` and `(3)` at every one of the
four q-slice points.

## Off-common intersections

After exact factor classification, projections `01`, `02`, and `03` have
`2`, `1`, and `1` residual cofactors. The two possible triples give
`t`-norms of degrees 62 and 179. Their support factors into four and seven
linear polynomials, respectively. Endpoint gcd and deduplication leave seven
distinct `(p,t)` values. Every value kills the explicit base forbidden
product, so none reaches the `w` gate.

The open factors, linear component, quartic component, and both residual
projection intersections exhaust the factorization, proving the claim.
