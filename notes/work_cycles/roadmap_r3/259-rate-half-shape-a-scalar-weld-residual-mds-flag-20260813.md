# Cycle 259: rate-half Shape-A scalar-weld residual-MDS flag (2026-08-13)

The static-source arbitrary-drop fence from Cycle 257 showed that the
bordered Hankel flag cannot be bounded one fiber at a time. The all-excess
factorization and the unique scalar weld now remove that fiberwise freedom.

Write every classified split row as

```text
G(t,x)=lambda_xP_x(t),
```

where `lambda` is the single projective row-scalar vector recovered by a
passing connected weld. For an off-line slope `delta`, divide these row
values on `X_delta=U_0\I_delta` by the known actual-support and padding
factors. The resulting vector is exactly

```text
(zeta_delta H_delta(x))_(x in X_delta).
```

Lagrange leading-coefficient extraction therefore proves that the fiber
degree drop `q_delta` is the exact initial zero-run length of an explicit
residual-RS parity flag applied to the same `lambda`. The first parity is at

```text
j_delta=3e+r_delta-1,
```

and the parity after the run is `zeta_delta lc(H_delta)!=0`. Consequently

```text
deg T=e-sum_delta q_delta
```

is now a stacked linear flag on one weld vector, not a collection of
independent residual choices.

```text
start:                   dc77d82bed8117edb629e07328abf9d489bdb2b5
canonical prize:         fdfb20a42 (clean; unchanged)
upstream Lane-T head:    PR #1161 at 4ecdbbc
result:                  PROVED scalar-weld residual-MDS flag
DAG delta:               +1 PROVED node, +4 req edges, +1 evidence edge
critical status delta:   none; rate_half_band_crossing_location remains open
primary replay:          F_101, drops 0..3, 22 parities, 108 row checks
independent replay:      F_127, degrees 2,1,0 with separate interpolation
hostile mutations:       8/8 normal and optimized
compute:                 constant-size local exact arithmetic; no Modal spend
next route action:       bound the stacked extra-parity rows on the unique
                         weld vector using incidence/collision structure
```
