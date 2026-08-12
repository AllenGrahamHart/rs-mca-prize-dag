# `A=1` quadratic nonreduced higher-corank Smith/jet router

- **status:** PROVED
- **closure:** exact three-profile router away from quotient-root collision
- **consumer:** `rate_half_band_crossing_location`

Retain an unshared nonreduced correction at `tau`, with obstruction jets
`kappa_2,kappa_3`, regular symmetric block `N(z)`, and divided row `U`.
Suppose

```text
(kappa_2,kappa_3)!=(0,0).                          (HSR1)
```

Put `r=corank N(0)`. Let `P_tau` be the minimal polynomial of the
specialized truncated moment recurrence, and assume `r>=2`. There is a
degree-`r-1` polynomial `L_tau` such that

```text
2<=r<=4,
deg P_tau=d-r,
U_tau=P_tau L_tau,
Q_tau=P_tau(X-x_*)L_tau.                           (HSR2)
```

Thus the quotient-root collision is exactly

```text
U_tau(x_*)=0
 iff P_tau(x_*)L_tau(x_*)=0.                       (HSR3)
```

Its two possible sources are a compressed-recurrence collision
`P_tau(x_*)=0` and a residual collision `L_tau(x_*)=0`.

Away from this collision, every nonzero-jet survivor has exactly one of
the following regular Smith/jet profiles:

```text
Smith [1,3]:     kappa_2=0,       kappa_3!=0;
Smith [2,2]:     kappa_2!=0;
Smith [1,1,2]:   kappa_2!=0.                           (HSR4)
```

In particular, regular corank four, whose only possible profile is
`[1,1,1,1]`, forces both jets to vanish and is excluded by `(HSR1)`.
No noncollision survivor has regular corank greater than three.

## Scope

The theorem assumes rather than derives `r>=2`. It does not exclude either
source of quotient-root collision or any of the
three profiles in `(HSR4)`. Diagonal symmetric germs realize each abstract
Smith/jet behavior, so their exclusion requires the retained Hankel/source
or split-fiber geometry. A nonreduced root shared with `g_*` is not covered.
