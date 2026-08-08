# Proof

Fix a source-sign pair and target lane. Work on the proved cell-4 tower over
`F_p(r)` with basis `1,t,b,bt`, quadratic relations for `t` and `b`, and
linear recovery of `c`. Reduced FLINT fractions retain every numerator and
denominator introduced by inversion.

For `xi=0`, the residual product list is

```text
de, -de, df, sigma_o ef, bf, sigma_c cf.
```

At matching 14 the first two equations share `f`:

```text
P_b(f) = Pair(-de,bf),
P_c(f) = Pair(de,sigma_c*cf).
```

Both are quadratic in `f`. If their coefficients are
`p_b0,p_b1,p_b2` and `p_c0,p_c1,p_c2`, their division-free resultant is

```text
(p_b2*p_c0-p_b0*p_c2)^2
 - (p_b2*p_c1-p_b1*p_c2)*(p_b1*p_c0-p_b0*p_c1).       (1)
```

It vanishes whenever the two cuts have a common root, including every
leading-degree drop. Taking the four-dimensional tower norm of (1) gives a
necessary target-free cut.

For every root of the norm numerator, norm denominator, or an inversion-
guard numerator or denominator, the compiler lifts the original `t`, `b`,
`c`, and compact-kernel equations. At each guarded source point it solves
both scalar quadratics and intersects their complete root sets. For a common
root `f`, put `u=ef`. The omitted product and squared sum give

```text
(u^2 + de*f^2)^2 - s*f^2*u^2 = 0.                   (2)
```

Equation (2) is an even quartic. The direct replay enumerates all of its
base-field roots, reconstructs `e=u/f`, `d=de/e`, and evaluates the final
matching-14 equation

```text
Pair(df,sigma_o*ef).
```

The exact ledger has 152 candidate `r` values and 80 guarded source points.
The common quadratic intersections and quartic lifts produce 128
nonboundary candidates. Every candidate has a nonzero final paired cut.
There is no target boundary, witness, or unresolved branch, so `xi=0` is
empty.

The independent verifier recomputes the two quadratic root sets, their
intersection, and the even-quartic roots through a quadratic in `u^2` plus
modular square roots. It also reconstructs and reevaluates the final cut.
Thus the terminal labels are not trusted as certificates.

Deleting the other positive `DE` copy preserves the residual products,
missing squared sum, matching, and guards value-for-value. The 16 `xi=1`
cases therefore transport from `xi=0`, proving all 32 cases. QED.
