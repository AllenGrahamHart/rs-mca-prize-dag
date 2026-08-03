# Proof

## Exact fiber extremum

The fiber cap from the mixed core/block payment gives

```text
1<=m_i<=ell,       sum_i m_i=r.                      (1)
```

Choosing one point from each of three distinct fibers proves the equality in
`(FSP1)`.

For the extremum, hold all multiplicities except two, say `a>=b`, fixed.
If one unit is transferred from `b` to `a`, the terms involving both chosen
fibers change by

```text
((a+1)(b-1)-ab) sum_(j outside {a,b})m_j
 =(b-a-1) sum_(j outside {a,b})m_j<=0.               (2)
```

All terms involving only one of `a,b` depend on `a+b` and do not change.
Thus concentrating mass, subject to the cap `ell`, cannot increase the third
elementary symmetric function.  Repeating the transfer produces the packed
profile

```text
(ell,...,ell,u)       if u>0,
(ell,...,ell)         if u=0,
```

and its third elementary symmetric function is `T_pack`.  This proves
`(FSP2)`.

If at least three fibers must remain positive, the same transfers stop at
the most concentrated admissible profile.  For `r<=ell+2` it is

```text
(r-2,1,1),
```

and for `ell+2<r<=2ell` it is

```text
(ell,r-ell-1,1).
```

Their third elementary symmetric functions are the first two lines of
`(FSP3)`.  For `r>2ell`, the unrestricted packed profile already has at
least three positive parts, so `(FSP2)` is sharp under the extra condition.
This proves `(FSP3)`.

## Split-pencil endpoint

A point `x` has `phi(x)=[a:b]` exactly when

```text
(bP-aQ)(x)=0.                                        (3)
```

The pencil member is nonzero by coprimality of `P,Q`, and has degree at most
`ell`.  Every linear factor `X-x` occurring in the square-free block locator
therefore divides the pencil member associated with its fiber.  Multiplying
over the distinct fiber values proves `(FSP4)`.  The degree bound gives
`r<=ell` in the one-fiber case.  In the two-fiber case, both part sizes are
positive, at most `ell`, and sum to `r`, which is exactly `(FSP5)`.

## Incidence routing

Every parameter of affine dimension `s` owns at least `B_(s-2)` independent
core cuts to residual affine planes.  Choose one high-fiber selected block
for each member of `Tau_3`; `(FSP3)` supplies at least `T_+` triples on that
block.  The affine-plane component payment proves that a fixed core cut and
fixed distinct-fiber point triple own at most three target parameters.
Double counting proves `(FSP6)`.

If `r>2ell`, a union of two fibers contains at most `2ell<r` points.  Hence
every selected block is high-fiber.  There are at least two disjoint selected
blocks per target, and each supplies at least `T_pack` triples by `(FSP2)`.
The same count with this extra factor two proves `(FSP7)`.

If a target is not in `Tau_3`, all its selected blocks have at most two
fibers.  The active-defect router supplies at least two disjoint such blocks,
and `(FSP4)` gives the asserted split-pencil divisors.  No count of these
divisor choices has been used.  QED.
