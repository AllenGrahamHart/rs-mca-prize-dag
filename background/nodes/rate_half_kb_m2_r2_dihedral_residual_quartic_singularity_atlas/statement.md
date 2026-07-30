# KoalaBear m2 r2 residual quartic singularity atlas

- **status:** PROVED
- **scope:** the one-parameter `n=3,6` coefficient quartics `Q_(a,b)`
- **dependency:**
  `rate_half_kb_m2_r2_dihedral_residual_one_parameter_quartic_normal_form`
- **consumer:** `rate_half_band_closure`

For

```text
a in {-1,1},       b notin {-2,2},
```

every quartic `Q_(a,b)` in the residual normal form is geometrically
irreducible and rational.

If `b!=a`, its complete singularity set consists of three ordinary nodes:

```text
(S,P)=(0,-1),
P=0,       S^2=(a-2)/(a-b).                        (KBMS-1)
```

Each node has delta one. If `b=a`, the first point remains an ordinary node
and the other two coalesce at `[S:P:U]=[1:0:0]` into a tacnode of delta two.
The total delta is three in both cases, so the normalization has genus zero.

Thus coefficient-curve factorization and genus delete no allowed parameter.
The residual frontier is the six-pole and complete-source locator
realization inside these irreducible rational quartics.

No `n=3`, `n=6`, `m=2`, endpoint, KoalaBear, or Prize row is closed, and no
owner or payment is constructed.

## Falsifier

An allowed parameter producing a reducible quartic, an additional
singularity, a degenerate tangent cone at one of `(KBMS-1)`, or geometric
genus different from zero.
