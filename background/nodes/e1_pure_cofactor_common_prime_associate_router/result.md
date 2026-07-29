# Result

`PROVED`.  Every currently live prize profile-`(3,6,S=18)` collision at one
fixed row and quotient root becomes, after exact division by
`(1-zeta_256)^mu`, a generator of the same principal prime ideal.  Any two
such normalized values differ by an algebraic unit of `Z[zeta_256]`.

Within one cofactor, both that unit and its inverse have power-basis
coefficients in the exact row box
`[-floor(18^64/(2^mu p)),floor(18^64/(2^mu p))]`. The uniform prize bounds
are `1006,503,251,125` for cofactors `2,4,8,16`.

Modulo the 256 roots of unity, those associates also inject into the rank-63
unit log lattice inside the exact row body

```text
||lambda(u)||_1 <= 2(D+sqrt(128D)),
D=log(18^64/(2^mu p)).
```

That full lattice now has the explicit integer basis

```text
eta_a=zeta_256^((1-a)/2)(1-zeta_256^a)/(1-zeta_256),
a=3,5,...,127,
```

because the conductor-256 real class number is unconditionally one. Thus
each orbit has one unique exponent vector in `Z^63`; no unknown unit index
remains.

Each log-lattice point represents one 256-vector shift/sign orbit. The exact
profile contribution is `128 M_33(3,6)` edges per orbit, so the complete edge
budget necessarily requires at most 367 such orbits across cofactors
`2,4,8,16`; 368 already exceed the full allowance.

This replaces unrelated per-vector norm divisibility by one explicit
common-prime circular-unit associate family. It does not bound that family,
the weighted collision sum, or the E1 image.
