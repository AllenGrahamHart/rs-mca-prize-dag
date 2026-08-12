# Proof

The root normal form gives the exact normalized divisors

```text
div_C(X-x_*)=R_*+3B,
div_C(s_F)=R_*+2B.                                 (1)
```

Because `g_*(tau)!=0`, no point of `R_*` lies over `tau`. Hence for every
point `b` in `(NCD2)`,

```text
ord_b(X-x_*)=3m_b,
ord_b(s_F)=2m_b.                                   (2)
```

The restriction of the canonical Pade numerator `P_F` differs from `s_F`
only by the fixed domain-infinity contact, which is a unit at the finite
heavy row. Therefore

```text
ord_b P_F(t,X(t))=2m_b.                            (3)
```

Since `P_F` is polynomial in `X`,

```text
F_0(t)-P_F(t,X(t))
 =P_F(t,x_*)-P_F(t,X(t))
```

is divisible on the curve by `X-x_*`. Equations `(2)--(3)` show that the
difference has order at least `3m_b`, strictly greater than `2m_b`.
There can be no cancellation of the leading contact term, so

```text
ord_b F_0(t)=2m_b.                                 (4)
```

The left side of `(4)` is the pullback of a base polynomial. If
`s=ord_tau F_0`, then it equals `e_b s`. This proves `(NCD3)`; it also
proves that `F_0` is not the zero polynomial.

The two-jet theorem gives `s>=2`. The positive multiplicities in `(NCD2)`
sum to two, so there are only two divisor patterns.

If `B=b_1+b_2` with distinct points, `(NCD3)` gives

```text
e_(b_i)s=2       (i=1,2).
```

Thus `s=2` and both ramification indices are one. If `B=2b`, then

```text
e_b s=4,
```

so either `(e_b,s)=(1,4)` or `(2,2)`. This proves the asserted alternatives
for the normalized divisor and `F_0`.

When `s=4`, the two obstruction coefficients at orders two and three both
vanish. The two-jet theorem then gives local divisibility by `D_1` and
regular Smith type `[4]`.

When `s=2`, the coefficient `kappa_2=[z^2]F_0` is nonzero. It remains to
identify the locator collision. The specialized locator `Q(tau,X)` is
nonzero, so the parameter fibre has no vertical component. For a reduced
plane curve, the multiplicity of `x_*` in this finite fibre is the
intersection multiplicity with `t=tau`, hence the sum of `e_b` over
normalization branches mapping to `(tau,x_*)`. Equation `(1)` shows that
these are exactly the points in the support of `B`, because no `R_*` point
lies over `tau`. In both `s=2` subcases that sum is two. Thus

```text
ord_(X=x_*)Q(tau,X)=2.                             (5)
```

Since `Q_tau=(X-x_*)U_tau`, equation `(5)` is exactly
`U_tau(x_*)=0` with a simple residual factor in `U_tau`. This proves
`(NCD4)`. The complete dichotomy excludes `(NCD5)` and finishes the proof.
QED.
