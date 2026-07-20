# Proof

The reverse-residual theorem applied with first nonzero centered coefficient
`q=4` and degree gap `r-deg V=1` gives

```text
deg T=r.                                               (1)
```

Let `v_0` be the nonzero leading coefficient of `V`. In `C`, the
leading coefficients of the two displayed terms are

```text
4(r-1)v_0,       (4-d)v_0.
```

Their sum is `(4r-d)v_0=-4v_0`, which is nonzero under the characteristic
hypothesis. Hence

```text
deg C=r+3.                                             (2)
```

Put `A_0=DU^4` and `S=e_4DV^4`. The definition of `T` gives

```text
TU^3+d=dA_0-YA_0'+d.                                  (3)
```

Since `A_0+S=Y^d-1`, substitution in `(3)` cancels the binomial Euler
term and yields

```text
TU^3+d=YS'-dS
       =e_4V^3(4YD V'+V(YD'-dD))
       =e_4V^3C.                                      (4)
```

This proves the cubic identity. Any common nonconstant factor of `TU` and
`VC` would divide both sides of

```text
TU^3-e_4V^3C=-d,
```

and hence divide the nonzero field scalar `d`. This proves the gcd assertion.

The converse is also exact. Starting from `(4)` and reversing the displayed
calculation gives

```text
dQ-YQ'+d=0,       Q=D(U^4+e_4V^4).                    (5)
```

The polynomial `Q` is monic of degree `d`: the term `DU^4` is monic of
that degree, while `DV^4` has degree `d-4`. For every degree
`0<m<d`, the coefficient equation in `(5)` is
`(d-m)[Y^m]Q=0`; all these coefficients vanish because the characteristic
exceeds `d`. The constant equation gives `[Y^0]Q=-1`, and monicity gives
`[Y^d]Q=1`. Thus `Q=Y^d-1`, proving the converse.

Differentiate `(4)`. With the definitions in `(PER4)`,

```text
U^2W=e_4V^2Z.                                         (6)
```

Since `gcd(U,V)=1`, equation `(6)` gives `V^2|W`. If `t_0` is the
leading coefficient of `T`, then the leading coefficient of `W` is

```text
(r+3r)t_0=4rt_0,
```

which is nonzero because the characteristic exceeds `4r+4`. Therefore
`deg W=2r-1`. Since `deg V^2=2r-2`, there is a nonzero linear polynomial
`L` with

```text
W=V^2L.                                               (7)
```

Substitution in `(6)` and cancellation of `V^2` gives
`e_4Z=U^2L`. Also

```text
(TU^3)'=U^2W=U^2V^2L,                                 (8)
```

proving `(PER5)`.

Let `ell` be the unique root of `L` over an algebraic closure. Equation
`(8)` says that every finite critical point of `Phi=TU^3` is a root of
`U`, `V`, or `L`. A root of `U` maps to zero. At a root of `V`,
equation `(4)` gives `Phi=-d`. The only remaining critical point is
`ell`, proving `(PER6)`.

Finally, `U,V` are squarefree by the pure degree-rigidity theorem. A
repeated root of `T` outside `U` is a zero of `Phi'` outside `U,V`,
so it must be `ell`; the same argument applied to
`Phi+d=e_4V^3C` handles repeated roots of `C`. If a root is common to
`T,U`, its order in `Phi'` is at least three, whereas `U^2` contributes
only two orders in `(8)`; it must also be the root of `L`. The argument
for a root common to `C,V` is identical. Since `L` is linear, all such
defects are confined to one point. This completes the proof. QED.
