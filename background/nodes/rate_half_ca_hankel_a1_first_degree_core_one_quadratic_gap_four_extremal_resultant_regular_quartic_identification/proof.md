# Proof

Use the Pade syzygy

```text
QB-Lambda G=L P_F.                                  (1)
```

On the generic locus let `a=lc_X Q` and let `r_1,...,r_d` be the roots of
`Q`. Taking root products in `(1)` gives

```text
Res(Q,L)Res(Q,P_F)
 =c Lambda^d a^(n_0+d-1-n)Res(Q,G),                (2)
```

where `n_0=deg L=3p-2`. The degree identity

```text
n_0+d-1-n=2d+1                                     (3)
```

and the Pade resultant formula

```text
Res(Q,P_F)=c_F a^(2d+1)D_1                         (4)
```

cancel the complete leading-coefficient power in `(2)`. Polynomial
continuation gives `(ERQ2)` on every fiber.

Because `L` is the monic locator of `U_0`, resultant symmetry gives

```text
Res_X(Q,L)=c product_(x in U_0)Q(t,x).              (5)
```

For `x in M_gamma`, the row `Q(t,x)` has the `e-2` off-line actual-support
roots and the two center roots different from `gamma`. If `d_A=0`, the
exceptional row has all three center roots and its `e-3` off-line roots.
Counting row incidences therefore yields

```text
product_(x in U_0)Q(t,x)
 =c [product_(gamma in A)ell_gamma^(d-r_gamma)]
    [product_(delta off line)
             ell_delta^(n-a_delta-r_delta)].       (6)
```

Both quadratic root arms have the exact regular-factor decomposition

```text
D_1=c E_4 product_(gamma supported)ell_gamma^r_gamma.
                                                               (7)
```

Indeed the supported product is `g_*` in the double-root arm and `G_1G_2`
in the two-simple arm, with overlap multiplicity equal to `r_gamma`.

Insert `(6)--(7)` into `(ERQ2)`. At each center slope the exponent is

```text
(d-r_gamma)+r_gamma-d=0,                            (8)
```

while at an off-line slope it is

```text
(n-a_delta-r_delta)+r_delta=n-a_delta.              (9)
```

This proves `(ERQ3)`.

The factor after one copy of every actual-support and padding point has
projective degree four. Formula `(ERQ3)` says its complete parameter norm is
the binary quartic `E_4`, proving `(ERQ4)`. Finally substitute
`E_4=cS_B^2` or `E_4=cS_1S_2` from the Pade regular-factor theorem to obtain
`(ERQ5)`. Homogeneous resultants retain the parameter-infinity fiber, so no
additional loss is possible. QED.
