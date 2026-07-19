# Proof

Reverse the centered norm equation and absorb the nonzero leading coefficient
of `V` into the outer parameters. Since `e_2=0,e_3!=0`, valid intermediate
data satisfy

```text
Q=B^4+theta z^(3h)B Cbar^3+phi z^(4h)Cbar^4,           (1)
```

where `Cbar(0)=1`, `theta!=0`, and `deg Cbar<=v=2h-2`.
Subtracting `B^4`, dividing by `z^(3h)`, and evaluating at zero identifies
`theta=Rbar(0)`. Divide the result by `theta B` and put `u=phi/theta` to obtain

```text
H=Cbar^3(1+u z^h Cbar/B).                              (2)
```

For fixed `u`, equation `(2)` has a unique normalized formal solution. Indeed,
at `z=0,C=1` its derivative with respect to `C` is three, which is invertible
because the characteristic exceeds `d`. Coefficient recursion, or formal
Hensel lifting, proves existence and uniqueness of `C_u` in `(IHC5)`.

The solution at `u=0` is the normalized cube root `C_*`. Write

```text
C_u=C_*+u z^h D mod z^(2h).                            (3)
```

Terms involving two copies of `z^h` vanish modulo `z^(2h)`. Substitute `(3)`
in `(IHC5)` and use `H=C_*^3`. The coefficient of `u z^h` gives

```text
3C_*^2D+C_*^4/B=0,
```

so `D=-C_*^2/(3B)`. This is `(IHC6)`.

A valid `Cbar` has degree at most `2h-2`, hence its coefficient at `2h-1`
vanishes. Extract that coefficient from `(IHC6)`. The first term contributes
`kappa`; after removing `z^h`, the correction contributes
`-(u/3)Delta`. This proves `(IHC7)` and all three alternatives in `(IHC8)`.

If a scalar survives, formal uniqueness makes `C_u=Cbar`. Polynomiality with
the printed degree bound and the exact multiplied version of `(IHC5)` recover
equation `(1)`. The elementary symmetric functions of the scaled centered
outer parameters are `(0,theta,theta u)`, giving `(IHC9)`. Distinct splitting
and the fractional-linear matching then reconstruct the two locator relations
exactly as in the generic canonical-span converse.

Conversely, the printed polynomial, identity, splitting, and matching reverse
these steps and invoke the antipodal-descent converse, proving sufficiency.

For scaling, replace `b_i` by `lambda b_i`, `lambda^d=1`. The fourth-root
covariance gives

```text
B_lambda(z)=B(lambda z),
Rbar_lambda(z)=lambda^(3h)Rbar(lambda z),
H_lambda(z)=H(lambda z),
C_*lambda(z)=C_*(lambda z).
```

Thus `Delta_lambda=lambda^(h-1)Delta` and
`kappa_lambda=lambda^(2h-1)kappa`, while
`u_lambda=lambda^h u`. Equation `(IHC7)` scales by the common nonzero factor
`lambda^(2h-1)`, preserving `(IHC8)`. A square root of `lambda` exists in the
official order-`4d` domain, so the Möbius matching transports as before. QED.
