# `A=1` quadratic extremal resultant regular-quartic identification

- **status:** PROVED
- **closure:** exact parameter eliminant for the four-core
- **consumer:** `rate_half_band_crossing_location`

Retain the extremal paired profile. Put

```text
d=deg_X Q=3e-2,       n=deg_X G=p-3,
L(X)=L_U0(X),         Lambda=ell_alpha ell_beta ell_theta.
                                                               (ERQ1)
```

For one nonzero scalar `c`, the homogeneous `X`-resultant is

```text
Lambda(t)^d Res_X(Q,G)
 =c D_1(t) Res_X(Q,L).                              (ERQ2)
```

Let `ell_delta` cut out an off-line supported slope, with union excess
`a_delta`. Then the complete factorization is

```text
Res_X(Q,G)
 =c E_4(t) product_(delta off line)
                   ell_delta(t)^(n-a_delta).        (ERQ3)
```

Thus the parameter pushforward of the residual projective intersection
cycle `Z_4` is exactly

```text
pi_*Z_4=div(E_4).                                   (ERQ4)
```

Combining with the Pade regular-factor theorem gives

```text
double root:  pi_*Z_4=2 div(S_B),
two simple:   pi_*Z_4=div(S_1)+div(S_2).            (ERQ5)
```

The identities include repeated and shared roots. In particular there are
no residual parameter fibers outside the correction quartic, and no
projective-infinity loss hidden by the affine resultant.

## Scope

`(ERQ5)` identifies the parameter fibers carrying the four units; it does
not by itself identify every local point when a correction root is a center
slope, nor does it exclude either correction pattern.
