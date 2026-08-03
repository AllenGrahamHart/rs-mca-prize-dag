# Proof

Use target variables

```text
a=de,  u=df,  v=ef,  f=f,             a f^2 = u v.       (1)
```

The parent structure theorem supplies, for each source-sign row, a guarded
curve

```text
F(r,b)=F_2(r)b^2+F_1(r)b+F_0(r)=0,
```

rational maps for `t,c`, and a global normalized common kernel. At the
missing source label `xi=-t^2`, write its two kernel evaluations as
`A_xi,B_xi`. The omitted product row requires

```text
B_xi = y_i A_xi.                                      (2)
```

On `A_xi!=0`, this fixes the missing record to `m=B_xi/A_xi`. If `df` or
`ef` is missing, equation (1) eliminates the other of `u,v`. If `bf` or
`cf` is missing, the nonzero guarded target label `f` is fixed by (2), and
(1) eliminates `a`. Thus every case has only two free target variables.

Reduce the rank-one equation, the three residual-pair Vieta determinants,
and the missing squared-sum equation in the quadratic pair algebra
`F_p(r)[b]/(F)`. Every reduced equation has the form `C_i+bL_i`. Choose a
nonzero cutter `C+bL`. Every solution necessarily annihilates

```text
C_i L-L_i C,                    for every other equation,              (3)
F_2 C^2-F_1 C L+F_0 L^2.                                             (4)
```

The exact compiler uses three complete structural classes.

1. For missing `df` or `ef` and matching zero, two projections in (3) are
   univariate in the same target. Their resultant is a nonzero `H(r)`.
   This covers 32 cases.
2. For missing `df` or `ef` and matchings 1 through 14, one projection is
   univariate in an outer target. A resultant of two mixed projections,
   followed by a resultant with that univariate projection, gives a nonzero
   `H(r)`. This covers 448 cases.
3. For missing `bf` or `cf`, one projection is already a nonzero target-free
   `H(r)`. This covers 480 cases.

For every `H`, FLINT computes

```text
gcd(H(r), r^2130706433-r),
```

and factors this square-free polynomial exactly. Hence the ledger lists all
base-field parameter roots, not a sample. Established route-guard roots are
discarded. At every other root, the compiler specializes the original
reduced equations, forms all pair crosses and quadratic-curve resultants,
enumerates every remaining target root and every `b` root over the deployed
field, and finds no solution.

The aggregate ledger contains 960 complete cases and 12,880 parameter-root
incidences. Of these, 10,032 are established guard boundaries and 2,848 are
checked directly. All 2,848 direct fibers are empty. The checker also
decompresses and hash-verifies every stored eliminant and verifies the full
Cartesian case set. An independently written FLINT replay reparses every
stored eliminant and recomputes every `gcd(H,r^p-r)`; all 960 root sets and
all 12,880 roots agree exactly with the primary compiler.

It remains to justify the two divisions introduced by the quadratic and
missing-record charts. A separate division-free compiler checks the leading
coefficient `A(r)` of `F`: across all four source signs its eight deployed
roots are route boundaries. It then clears the `t` denominator in
`A_xi,B_xi` and checks the original boundary

```text
F(r,b)=A_xi(r,b)=B_xi(r,b)=0.                            (5)
```

The necessary cross/norm gcds have 24 deployed roots across the four signs,
all route boundaries. Thus (5) has no guarded point. The remaining
inversions are the globally valid `t,c` and kernel denominators from the
parent theorem or nonzero target products from the target guards. No live
component is removed. Therefore all 960 systems are empty. QED.
