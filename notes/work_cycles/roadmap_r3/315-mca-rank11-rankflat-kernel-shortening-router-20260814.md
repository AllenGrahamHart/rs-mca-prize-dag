# Cycle 315: MCA rank-11 rank-flat kernel shortening (2026-08-14)

The new PROVED node
`rate_half_mca_rank11_relative_rankflat_kernel_shortening_router` classifies
the remaining individual positive-dimensional components.

For a correction space `W`, `2<=s=dim W<=10`, and an `s+1` coordinate flat
`T`, put

```text
U=ker(ev_T:W->F^T),       u=s-rank(ev_T).
```

Rank-zero evaluation cannot support a slope-dominating component: the
coordinate equations reduce to nonzero core error polynomials and have
finite slope projection. A vertical component costs one slope.

On a slope-dominating component, choose a complement `W_0` to `U` and solve
the coordinate equations there. High-core absorption puts every remaining
high coefficient in `U`; the low coefficients define one affine codeword
owner agreeing with the received line on `T`. After translation, all
component explanations lie in `U` and vanish on `T`.

Exact division by the locator of `T` gives a shortened family with

```text
u<=s-1<=9,
n''-K''=1048576,
m''-K''=67472.
```

Cycle 310's uniform rank-drop theorem pays it. Thus every individual
rank-flat component is either vertical or paid after kernel shortening.

Focused verification:

```text
RATE_HALF_MCA_RANK11_RELATIVE_RANKFLAT_KERNEL_SHORTENING_ROUTER_PASS
  rank=2 kernel=1 paid_to=9 controls=6/6
RATE_HALF_MCA_RANK11_RELATIVE_RANKFLAT_KERNEL_SHORTENING_ROUTER_AUDIT_PASS
  kernel_max=9 vertical=1 controls=4/4
```

No numerical experiment or Modal computation was used.

```text
start:                   a5ca83bed
DAG delta:               +1 PROVED rank-flat shortening router,
                         +2 requirement edges, +1 evidence edge
critical status delta:   none
upstream terminal delta: all individual H_C components routed
delta-star movement:     none
compute:                 exact kernel/complement linear algebra only
next route action:       build chronology/compatibility controlling the
                         aggregate mass of component and affine owners
```
