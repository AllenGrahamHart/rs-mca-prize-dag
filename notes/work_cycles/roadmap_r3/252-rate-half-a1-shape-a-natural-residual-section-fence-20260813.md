# Cycle 252: rate-half shape-A natural residual-section fence (2026-08-13)

The rigid four-cycle from Cycle 250 can exclude shape A only if the source
supplies a second section of `O_C(2B)`. The four immediate candidates do not.

After the mandatory intersection divisor is removed, the restriction of
`G` is the unique canonical residual section. On `Q=0`, the Pade syzygy

```text
-Lambda G=L_U0 P_F
```

identifies the normalized `P_F` restriction with that same section.
It is not independent.

The raw first derivatives fail in the opposite way. A pure split fiber has

```text
G(delta,X)=zeta_delta A_delta(X)
```

with `n` distinct roots, and every classified row has distinct parameter
roots. Thus at every one of those mandatory actual-support points,

```text
G_X(delta,x)!=0,       G_t(delta,x)!=0.
```

Neither derivative contains even one copy of the mandatory divisor, so
formal division creates poles instead of a residual section.

```text
start:                   1e63bdaeb
canonical prize:         fdfb20a42 (clean; unchanged)
result:                  PROVED natural residual-section route fence
DAG delta:               +1 PROVED node, +4 req edges, +1 ev edge
critical status delta:   none; rate_half_band_crossing_location remains open
retired candidates:      G, P_F, raw G_t, raw G_X
remaining section route: a new combination restoring every mandatory zero
compute:                 constant-space local arithmetic only; no Modal spend
next route action:       attack the concentrated excess norm T and scalar weld
```
