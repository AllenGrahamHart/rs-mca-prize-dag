# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one singular-J-nonzero chart compiler

On `Delta=0`, `J!=0`, the router gives `W=0` and

```text
(q-d)D^2H+JK_6=0.                                   (1)
```

The inherited saturation has `(q-d)DJK_6!=0`, so (1) gives `H!=0`.
Moreover,

```text
Delta=G_2J+x(q-d)D.
```

If `x=0`, then `G_2J=0`, hence `G_2=0`. Conversely, if `G_2=0`, then
`x(q-d)D=0`, hence `x=0`. This proves (SJC1).

Suppose first that `x=G_2=0`. The definitions in (SQC1)--(SQC3) give
(SJC2). In particular `D=Y^3!=0`. The equation `W=0`, multiplied by 288,
is

```text
P_W^+=0.                                             (2)
```

The sixth equation becomes

```text
K_6+Y^6+L_3Y^3=0.                                   (3)
```

Using (3), equation (1) is equivalent, after cancelling `6Y^3`, to

```text
(q-d)Y+dY^3+dL_3=0.                                 (4)
```

Multiplication of (4) by 1728 gives

```text
P_F^+=576qd^2+(q^3+90q^2+7164q+57240)d
      +144q^2+4320q=0.                              (5)
```

Direct coefficient collection gives

```text
P_F^+=8P_W^++P_L^+.                                 (6)
```

Thus (2), (3), and (5) are equivalent to (SJC4), proving the first chart
and its two denominator cases.

Now suppose `x!=0`; then (SJC1) gives `G_2!=0`. Put
`Q_6=(Y-A)V-S`. On `W=0`, the fourth and sixth equations are

```text
DG_2H-xK_6=0,       DQ_6-K_6=0.                    (7)
```

Because `xD!=0`, equations (7) are equivalent to the first equation in
(7) and

```text
xQ_6-G_2H=0.                                        (8)
```

The definitions of `S,A` give the polynomial identity

```text
Q_6=6G_2+AxU-L_3-D.                                 (9)
```

Since `L_3=20+q(d+8)/3`, three times (8) is exactly

```text
P-qxd=0.                                            (10)
```

The determinant has the second useful identity

```text
Delta=(q-d)(G_2^2+xD)-6dDG_2=qN-dZ.                (11)
```

The inherited HNF saturation gives `q!=0`. Equations (10)--(11), together
with `x!=0`, therefore prove (SJC6). Also `N=0` in (11) would give
`dZ=6dDG_2!=0`, a contradiction; `Z=0` similarly contradicts `qN!=0`.

Conversely, reconstructing `d=P/(qx)` from a saturated solution of (SJC8)
makes (10) hold, while the first equation of (SJC8) makes (11) vanish.
The equations `W_hat=E_hat=0` recover `W=0` and the first equation in (7).
Equations (8)--(10) then recover `E_6=0`. Finally, on `Delta=0`,

```text
J=-x(q-d)D/G_2!=0,
(q-d)D^2H+JK_6=(q-d)D(DG_2H-xK_6)/G_2=0,           (12)
```

so the fifth equation and the required singular branch are recovered.
The last two equations of (SJC8) are exactly the retained conic and role
equation after reversible denominator clearing. This proves both directions
of the second chart. QED.
