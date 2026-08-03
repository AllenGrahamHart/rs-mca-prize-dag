# Proof

The seven outside records in canonical order are

```text
de, de, -de, df, sigma_o ef, bf, sigma_c cf.
```

Delete `xi=6`. The source quotient supplies the missing record `m` and its
squared sum `s`. If a target lift existed, write `g=sigma_c f`. Then

```text
m = cg,
s = c^2+f^2+2 sigma_c cf = (c+g)^2.
```

Multiplication by `c^2` clears the guarded division `g=m/c`:

```text
c^2 ((c+m/c)^2-s) = (c^2+m)^2-s c^2.
```

Thus the displayed polynomial is a necessary condition before any matching
or target-lane equation is imposed.

The compiler evaluates this condition in the exact six-dimensional quotient
with basis `1,t,t^2,b,bt,bt^2`. It first takes the quadratic norm in `b`, then
the cubic norm in `t`, obtaining a rational function of `r`. Every root in
the deployed field of its numerator is included. To retain every branch on
which quotient arithmetic may have divided, the candidate set also includes
every deployed-field root of every inverse-guard numerator and denominator
and of the base-cubic leading coefficient.

Each candidate `r` is lifted through the original base cubic, the original
quadratic `b` relation, linear `c` recovery, product-rank cofactors, and the
compact kernel. Missing-ratio-free branches are recorded unresolved rather
than discarded. At every recovered source point the compiler recomputes
`m`, `s`, and both the cleared and divided compatibility values, checking

```text
(c^2+m)^2-s c^2 = c^2 ((c+m/c)^2-s)
```

directly in the deployed field.

Across the four source signs, the census has 32 candidate `r` values and 32
recovered source points. Eight source points have `m=0` and are excluded by
the nonzero target guards. The remaining 24 points all have nonzero cleared
compatibility. There are no compatible points and no unresolved branches.
Therefore no `xi=6` target exists. Since the condition precedes and is
independent of all 15 matchings and all four target lanes, all 240 raw cases
are empty. QED.
