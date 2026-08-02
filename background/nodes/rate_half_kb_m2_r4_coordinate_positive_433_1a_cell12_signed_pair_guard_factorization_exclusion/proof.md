# Proof

Exact lex reduction of the guard-saturated cell-12 common ideal gives nine
basis elements.  Reducing all eight common-kernel coefficients and
eliminating the two linear coordinates gives

```text
deg_(b,t) P=(4,8),  terms(P)=17,  lc_b(P)=t^4.     (1)
```

All normalized coefficients have `b`-degree at most three, and exact
comparison gives `B1(-W)=-B1(W)`.  The paired-product theorem therefore
supplies the two complete necessary equations in `(KBC12-1)`.

Plane reduction of those equations takes three and nine steps.  Their raw
`w1` resultant has 153,761 terms and degrees `(16,18,592)` in
`(w0,b,t)`.  Fifteen more reductions give `R`, with 36,236 terms and
degrees `(16,3,672)`.  This is the full resultant, not a selected factor.

Construct `D0^5`, `rd^2w0-rn^2`, and the square of
`rd^2w0+rn^2`, reducing after each multiplication.  Each of the ten
reductions takes three steps.  Cross multiplication of the leading
coefficients then gives the exact zero remainder

```text
c16R-r16C congruent 0 (mod P).                    (2)
```

The exact norm of `r16` has degree 2432 and 1621 terms.  Its factorization
contains eight linear factors, three irreducible cubics, and one irreducible
decic.  Its base-field roots are exactly

```text
0, 1, i, 1117681606, 1419755025, 1992261782, -i, -1. (3)
```

The six values

```text
0, 1, i, 1117681606, -i, -1                       (4)
```

are exactly the base-field roots of a denominator, projective,
plane-leading, or projected common scale.  At the two roots in `(3)` not in
`(4)`, specialization of `gcd(P,r16)` gives four deployed `b` lifts.  Every
deployed root of `R(w0)` at those lifts has one of the guards

```text
N0, D0, w0+1, w0-r^2, w0+r^2;                    (5)
```

the remaining quadratic factors are irreducible.

Factorization of all six compact-kernel scales is exact.  Five roots in
`(4)` are `0,+/-1,+/-i`; direct replay in the original localized common
ideal gives `[1]`.  At the remaining value `t=1117681606`, the original
common ideal reduces to

```text
r=558459069,
c=460157884-40350282b,
b^2-9674473b+1=0.                                 (6)
```

The last polynomial has exactly the two deployed roots
`816507220,1323873686`.  Evaluate the original, unnormalized common kernel
at each point of `(6)`.  It is nonzero and still has `B1(-W)=-B1(W)`.
The complete raw signed-pair resultant has degree 16 and factors only into
the five guards in `(5)`; nonlinear factors are irreducible.  Hence the
proper exceptional fiber is also empty.

Away from `(3)`, equations `(KBC12-1)--(KBC12-3)` force `G=0`, contradicting
the original product, denominator, and source-label guards.  Equations
`(3)--(6)` cover every omitted point.  Exact source and duplicate-role
symmetry transports the exclusion to all eight rows of `[12,13]`. QED.
