# Proof

Fix a source-sign pair and target lane. Work on the proved cell-4 tower over
`F_p(r)` with basis `1,t,b,bt`, quadratic relations for `t` and `b`, and
linear recovery of `c`. Reduced FLINT fractions retain every numerator and
denominator introduced by inversion.

For `xi=0` and `xi=2`, respectively, the residual product lists are

```text
de, -de, df, sigma_o ef, bf, sigma_c cf,
de,  de, df, sigma_o ef, bf, sigma_c cf.
```

At matching 11 the first two equations share `f`. Put

```text
P_b(f) = Pair(de,bf),
P_c(f) = Pair(second_de,sigma_c*cf),
```

where `de=m, second_de=-de` for `xi=0` and `de=-m,
second_de=de` for `xi=2`. Both are quadratic in `f`. If their coefficients
are `p_b0,p_b1,p_b2` and `p_c0,p_c1,p_c2`, their division-free quadratic
resultant is

```text
(p_b2*p_c0-p_b0*p_c2)^2
 - (p_b2*p_c1-p_b1*p_c2)*(p_b1*p_c0-p_b0*p_c1).       (1)
```

It vanishes whenever the two cuts have a common root, including every
leading-degree drop. Taking the four-dimensional tower norm of (1) therefore
gives a necessary target-free cut.

For every root of the norm numerator, norm denominator, or an inversion-
guard numerator or denominator, the compiler lifts the original `t`, `b`,
`c`, and compact-kernel equations. At each guarded source point it solves
both scalar quadratics and intersects their complete root sets. For a
nonzero common root `f`, put `u=ef`. The omitted product and squared sum give

```text
(u^2 + eta*de*f^2)^2 - s*f^2*u^2 = 0,                (2)
eta = 1 for xi=0,  eta = -1 for xi=2.
```

Equation (2) is an even quartic. The direct replay enumerates all of its
base-field roots, reconstructs `e=u/f`, `d=de/e`, and evaluates the final
matching-11 equation

```text
Pair(df,sigma_o*ef).
```

The exact ledger has 304 candidate `r` values and 192 guarded source points.
The common quadratic intersections produce 16 `f=0` target boundaries and
64 nonboundary quartic candidates. Every nonboundary candidate has a
nonzero final paired cut. There is no witness or unresolved branch, so
`xi=0,2` are empty.

The independent verifier recomputes the two quadratic root sets, their
intersection, and the even-quartic roots through a quadratic in `u^2` plus
modular square roots. It also reconstructs and reevaluates the final cut.
Thus the terminal labels are not trusted as certificates.

Deleting the other positive `DE` copy preserves the residual products,
missing squared sum, matching, and guards value-for-value. The 16 `xi=1`
cases therefore transport from `xi=0`, proving all 48 cases. QED.
