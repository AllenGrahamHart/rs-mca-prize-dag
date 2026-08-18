# Cycle 464: rank-eleven heavy-plane Segre normalization

## Starting pins

```text
our SHA: 6c36b4ff3
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream split-pencil tip: PR #1170 at d296510e80
```

## Result: PROVED field-internal split-pencil normal form

The heavy residual plane has mass `9965407986` and at least 37,733 common
zeros after the rank-two triple cancellation. Cancelling its complete
locator gives a shortened row with

```text
4<=K<=1010840.
```

The two factor spaces `P,Q` both have dimension two and are base-free. Since
their product span has dimension four, multiplication is an isomorphism

```text
P tensor Q -> span(PQ).
```

Every correction evaluation column is therefore a Segre column and every
associated factor slice is one ruling plane `gQ`. The exact two-space cap
gives

```text
ceil(9965407986/248644099)=41
```

used projective factors.

The rank-four support-local envelope has one turning point at shortened
dimension 177,803. Checking both endpoints of the full dimension interval
gives

```text
margin 11: uniform cap 10166508078
margin 12: uniform cap  9319299072 < retained mass.
```

Thus one selected direction record has at most 11 exceptions.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +5 edges
critical status delta: none
route delta: heavy rank-4 plane -> field-internal Segre pencil, 41 factors, <=11 exceptions
new assumptions: none beyond the parent factor branch
next action: prove base-field descent or a descent-obstruction alternative, then attach the upstream census
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_segre_shortening_transversality/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_segre_shortening_transversality/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_segre_shortening_transversality/verify_audit.py
```
