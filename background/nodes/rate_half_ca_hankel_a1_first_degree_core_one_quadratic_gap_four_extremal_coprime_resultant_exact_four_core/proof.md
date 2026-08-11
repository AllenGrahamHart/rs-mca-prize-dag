# Proof

Cycle 148 gives

```text
R_QG=L_M^(e-2) E_circ P_(R,0) W_old,
deg W_old<=4+r_bad,                                (1)
```

where `E_circ=(X-x_circ)^(e-3)` for `d_A=0` and is one for
`d_A=1`, while `P_(R,0)` is the product of padding factors on the
zero-excess slopes.

The all-excess fiber theorem gives, for every positive-excess slope,

```text
Qbar(delta,X)=chi_delta A_delta B_delta R_delta,
G(delta,X)=zeta_delta A_delta H_delta R_delta.     (2)
```

Every root of `R_delta` is therefore a common point of the two curves. It
lies outside `U_0`, so its resultant factor was not removed by
`L_M^(e-2)` or `E_circ`. Multiplying these additional factors over all
positive-excess slopes shows that the complete padding product `P_R`
divides the residual resultant in `(1)`.

Its additional degree is exactly

```text
r_bad=sum_(a_delta>0)r_delta.                      (3)
```

Dividing `(1)` by these factors leaves the nonzero quotient `W_4` and
subtracts `r_bad` from the old cap. Thus

```text
deg W_4<=(4+r_bad)-r_bad=4,                        (4)
```

proving `(EFC1)--(EFC3)`.

For the projective count, the two curve bidegrees are

```text
(3e-2,e),       ((3e-7)/2,e-2).
```

Their total Bezout intersection number is

```text
I=(3e-2)(e-2)+e(3e-7)/2
  =(9e^2-23e+8)/2.                                 (4a)
```

On an off-line supported slope, the common-root polynomial
`A_delta R_delta` has degree

```text
(n-a_delta-r_delta)+r_delta=n-a_delta.             (4b)
```

There are `3e` such slopes and `sum a_delta=e`. The mandatory common
points therefore have total first-copy degree

```text
sum_delta(n-a_delta)=3en-e=(9e^2-23e)/2=I-4.       (4c)
```

The curves are coprime, so their projective intersection is a finite
effective cycle of degree `I`. Subtracting the mandatory first copies gives
an effective residual cycle of degree four, proving `(EFC4)`.

The complete vertical-fiber gcd from the all-excess theorem is

```text
A_delta R_delta.                                   (5)
```

All `A_delta` roots lie in `U_0`. In the `d_A=1` profile they lie in
`M`; in the `d_A=0` profile the only root outside `M` is the possible
exceptional row, already included in `E_circ`. All `R_delta` roots are
included in `P_R`. Hence every common point over a supported off-line
fiber is already among the mandatory factors.

Finally, local intersection multiplicity is additive in the resultant
order. Any multiplicity beyond the mandatory first copy at the displayed
points, or any other common point, remains after the mandatory factors are
removed and is charged to `W_4`. The universal first-jet identity proves
that every `A_delta` root is transverse, so it contributes no such excess.
Any root of `W_4` must therefore come from excess multiplicity at padding
or from a center-line, unsupported, or projective-infinity parameter
fiber. The affine resultant records the domain projection of the finite
part of `Z_4`, which explains `deg W_4<=4`. QED.
