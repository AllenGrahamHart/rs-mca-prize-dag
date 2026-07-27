# Proof

The proved `V=64` profile reduction leaves autocorrelation magnitude profile
`(3,5,1)` as one of three possible branches. Its four odd coefficients force
the common light geometry classified by the four-odd router: exactly 28,800
normalized light supports in 148 affine odd-unit orbits.

Fix one representative of each orbit. The three magnitude-two coefficient
positions can be any three of the remaining 124 positions. Multiplying every
coefficient by `-1` preserves all chord products, so fixing the first heavy
sign positive leaves 64 sign patterns. Translation and odd cyclotomic
automorphism preserve the autocorrelation magnitude profile, conductor, and
`M_3`; any negacyclic wrap signs are already covered by the 64 patterns.
Thus the exact representative coverage is

```text
148 * binom(124,3) * 64 = 2,937,494,528.              (2)
```

The production engine precomputes the 21 folded chord classes for each heavy
support, forms their signed sums, and retains precisely the vectors with
three magnitude-one, five magnitude-two, one magnitude-three, and no larger
autocorrelation coefficients. Across (2) it finds 29,238 retained vectors,
of which 15,440 have full conductor, and exact maximum `M_3=1392` in both the
unrestricted and full-conductor ledgers.

The audit engine independently multiplies `F(X)F(X^-1)` in
`Z[X]/(X^128+1)`. It checks constant coefficient 16 and all 63 negacyclic
antisymmetry identities before applying the profile predicate and computing
the weighted zero-sum third moment. It independently exhausts (2) and agrees
on every per-template count, conductor count, and maximum, hence in
particular on (1).

The exact rational cubic-Hermite certificate in the profile reduction has
strict positive norm margin through `M_3=1517`. Therefore
`M_3<=1392<1517` puts every candidate collision norm strictly below `2^250`.
The collision-norm criterion contradicts pair feasibility, so profile
`(3,5,1)` is impossible. QED.
