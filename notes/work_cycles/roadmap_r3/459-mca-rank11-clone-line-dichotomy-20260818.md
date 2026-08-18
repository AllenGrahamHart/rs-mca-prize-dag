# Cycle 459: rank-eleven clone/line dichotomy

## Starting pins

```text
our SHA: 18f16d0ff
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream rich-flat tip: PR #1173 at 2788d5ec3
```

Canonical and upstream state were rechecked before this cycle. No newer
result supersedes the local rank-eleven factor frontier.

## Result: PROVED quantitative branch split

The deep residual classes contribute weighted triple incidence

```text
E*C(37736,3).
```

A rank-three coordinate triple has a two-dimensional residual kernel, so
its complete first-owned mass is at most `R_4=63397365764`. Subtracting all
rank-three triples leaves exact rank-at-most-two incidence

```text
255859400991343449179217479656.
```

For clone cutoff 10,000, convex packing bounds all rank-one clone triples by
`18531303013296`; each clone bucket costs at most `R_8`. The remaining
incidence forces the exact dichotomy:

```text
projective clone size >=10001,
or a genuine rank-two triple carries >=777301822903 slopes.
```

The verifier also retains the parameterized cutoff formula. Clone-only
coverage first becomes arithmetically possible at cutoff 18,400.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +1 evidence edge
critical status delta: none
route delta: rank<=2 triple -> large clone / massive genuine line
new assumptions: none beyond the explicit base-free 2 x 5 branch
next action: build exact owner-preserving adapters for the two output horns
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_factor_flag_clone_line_dichotomy/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_factor_flag_clone_line_dichotomy/verify_audit.py
```
