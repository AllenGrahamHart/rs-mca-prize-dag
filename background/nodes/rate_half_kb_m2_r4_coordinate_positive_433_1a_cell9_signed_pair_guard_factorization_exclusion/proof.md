# Proof

The exact guard-saturated cell-9 lex basis has size eleven.  Reducing the
common-kernel coefficients and eliminating the linear `r,c` coordinates
gives a 45-term bidegree-`(4,8)` plane `P`.  All normalized coefficients
have `b`-degree at most three, and `B1(-W)=-B1(W)` exactly.

The paired-product theorem supplies the complete necessary equations.  They
take three and nine plane reductions.  Their raw `w1` resultant has 146,243
terms and degrees `(16,18,482)` in `(w0,b,t)`; fifteen more reductions give
`R`, with 36,876 terms and degrees `(16,3,587)`.

Construct the product in `(KBC9-1)` with seven recorded three-step
pseudo-reductions.  Cross multiplication of the leading coefficients gives
the exact zero remainder

```text
c16R-r16C congruent 0 (mod P).                    (1)
```

The norm of `r16` has degree 2344 and 2153 terms.  Exact factorization gives
five linear factors, two irreducible quadratics, and three irreducible
cubics.  Its base-field roots are precisely

```text
0,1,i,-i,-1.                                      (2)
```

All six compact-kernel scales factor exactly.  Their linear-root union is
also precisely `(2)`; every nonlinear factor is irreducible.  Adjoining each
of the five values to the original guard-saturated common ideal gives the
reduced basis `[1]`.  Hence no scale-zero common point is omitted.

Away from `(2)`, a signed pair forces `R=0`; equation `(1)` then forces the
guard product `(KBC9-1)` to vanish, contradicting original product,
denominator, or source-label guards.  The unit scale charts cover every
leading or reduction exception.  Exact root-sign and duplicate-role
symmetry transports the exclusion from cell 9 to all eight rows of cells 9
and 10. QED.
