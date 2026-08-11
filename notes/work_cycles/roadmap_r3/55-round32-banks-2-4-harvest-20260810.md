# Cycle 55: Round 32 banks 2-4 harvest (2026-08-10)

## Canonical source

Harvest canonical Fable commit `3edb8b31b` in full. It banks the
`rh_farca_upper`, `rh_residuals_close`, and `rh_fr_algebraic` audit packets
and appends their conclusions to the rate-half crossing target. The retained
pilot files are byte-for-byte canonical; the only cherry-pick conflict was
resolved by retaining both the earlier Haboeck custody correction and the new
banks 2-4 addendum.

## New proved leaf

Round 32's clean positive result is extracted from the large critical node as

```text
rate_half_fr_canonical_min_pair_union_bound  [PROVED].
```

If `W*=S_g union S_h` is a minimum pair union of the locator sets, then every
third supported slope obeys

```text
|S_gamma intersect W*|
 <=4rho-2a*-2o_gamma-o_g-o_h,
|S_gamma \ W*|
 >=2a*-3rho+o_gamma+o_g+o_h.
```

At the clean endpoint `rho=4m-1`, `a*=7m-1`, this is intersection at most
`2m-2` and outside spend at least `2m+1`. The proof is elementary
inclusion-exclusion. Independent exhaustive replays cover every three-set
family on five points and every four-set family on four points.

The older incidence fence is narrowed accordingly: it refutes the
arbitrary-`W` form only. Its witness `W` is not a pair union, while all 32896
pair unions in that witness satisfy the canonical inequality.

## Remaining rate-half wall

The canonical bound is valid but insufficient. Exact replay gives residual
factor `9/8` at `a=7m-1`, while the full-band maximum moves to
`a=(20m-2)/3` with factor `7/4`. At that argmax the proved intersection cap is
asymptotically `8m/3`; closure needs `5m/3`, a missing factor `8/5`.

The far-CA bank identifies the same structural boundary from another side:
`3n/4` is the tall/wide pencil boundary, classical counting stalls at
`sqrt(nk)`, and the open interior requires moving-kernel or deep-stratum
control. The residual bank reduces the live combinatorial obstruction to the
same algebraic frontier and records the exact official exceptional integer.
No critical status changes.
