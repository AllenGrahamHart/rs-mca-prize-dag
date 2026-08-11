# Cycle 63: rate-half incidence rational-trace fence (2026-08-10)

## Adversarial construction

At `m=2` over `F_97`, choose six inverse pairs in the order-32 subgroup and
set

```text
nu_x=x+x^(-1)=(x^2+1)/x.
```

An explicit seven-vertex outside-incidence completion gives nine slope rows
of size seven, one total deficiency unit, and a selected minimum pair union
`W` of size 12. All 36 pair unions are at least 12, pair intersections are
at most two, and the bad-overlap value is `2>1`.

Since the residual width is three, `P=X`, `Q=X^2+1` are an allowed rational
certificate. Exact rank computation gives

```text
rank(M_W)=11<12,
```

with a one-dimensional all-nonzero kernel. This falsifies any attempt to
promote the earlier random zero-exception profile into an incidence-only
full-rank theorem.

## Diagnosis and repair

The witness is not an actual Hankel pencil: its locator coefficient values
do not extend to `X`-degree seven. The Cycle-62 rows detect this exactly:

```text
rank([M_W;E_W])=12.
```

The proved node
`rate_half_bivariate_incidence_only_rational_trace_route_fence` therefore
redirects the official proof toward the strengthened matrix rather than
killing the bivariate route. The construction used one deterministic 256 MB
Modal task and has two standard-library local replayers. No critical status
changes.
