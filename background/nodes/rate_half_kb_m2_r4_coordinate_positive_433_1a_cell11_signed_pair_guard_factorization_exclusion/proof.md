# Proof

The exact guard-saturated cell-11 lex basis has size ten.  Reducing the
common-kernel coefficients and eliminating the linear `r,c` coordinates
gives a 45-term bidegree-`(4,8)` plane `P`.  All normalized coefficients
have `b`-degree at most three, and `B1(-W)=-B1(W)` exactly.

The paired-product theorem supplies the complete necessary equations.  They
take three and nine plane reductions.  Their raw `w1` resultant has 172,159
terms and degrees `(16,18,562)` in `(w0,b,t)`; fifteen more reductions give
`R`, with 42,316 terms and degrees `(16,3,667)`.

Construct the product in `(KBC11-1)` with nine recorded three-step
pseudo-reductions.  Cross multiplication of the leading coefficients gives
the exact zero remainder

```text
c16R-r16C congruent 0 (mod P).                    (1)
```

The norm of `r16` has degree 2664 and 2473 terms.  Exact factorization gives
ten linear factors, two irreducible cubics, and one irreducible septic.  Its
base-field roots are

```text
0,1,i,33199819,67070255,989155728,
1231496538,1620586492,-i,-1.                      (2)
```

The seven compact-scale roots are

```text
0,1,i,1231496538,1620586492,-i,-1.                (3)
```

At `33199819` and `67070255`, the only deployed `b` lift is the original
guard `b=-1`.  At `989155728`, there are two deployed lifts.  Exact
factorization of `R(w0)` at both lifts displays twelve base-field roots;
every root has at least one of

```text
N0=0, D0=0, w0=t^2, w0=r^2, w0=-r^2.             (4)
```

All six compact-kernel scales factor exactly.  The linear-root union is
precisely `(3)`; every nonlinear factor is irreducible.  Adjoining each of
the seven values to the original guard-saturated common ideal gives the
reduced basis `[1]`.  Hence no scale-zero common point is omitted.

Away from `(2)`, a signed pair forces `R=0`; equation `(1)` then forces the
guard product `(KBC11-1)` to vanish, contradicting original product,
denominator, or source-label guards.  Equations `(2)--(4)` and the unit
scale charts cover all exceptions.  Exact root-sign symmetry transports the
exclusion to all four cell-11 rows. QED.
