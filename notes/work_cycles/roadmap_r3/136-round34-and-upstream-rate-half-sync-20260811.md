# Cycle 136: Round-34 and upstream rate-half synchronization (2026-08-11)

## Cycle pins

```text
our source:       66360d01f
canonical prize:  6b337c6d17c63b557b2dd4c489aa938434033c3d
upstream main:    93fba1be3f3299b0ba4708d88715377bbb656e45
upstream PRs:     #1161 draft/mergeable; #1162 open/mergeable
critical open:    28
compute:          inspection only
```

## Canonical correction and new round

Canonical Round 33 has completed. Its main correction is that the proposed
far-CA forced-fixed-generator step is false: the shifted generators need not
form a minimal basis, so Forney's inequality gives no upper bound in the
claimed direction. Canonical withdrew `R-MOVING`, retained the stacked-rank
invariant, and launched a separate `p*` boundary pilot.

The other Round-34 pilots attack the full-domain Layer-A system, the `m=2`
saturation boundary, and the `m=3,4` bivariate-curve boundary. These are
parallel rate-half instruments. They do not alter the proved `A=1` quadratic
pair-boundary reductions, but they independently confirm that full-domain
bivariate compatibility is the route-deciding object.

Upstream main has not moved. PR #1162 retains the two-sided razor bracket,
and draft PR #1161 retains our fixed-domain paired-biform coefficient gate.

## Burn-down

```text
result:                  synchronized; false far-CA premise fenced
DAG delta:               none
critical status delta:   none
upstream terminal delta: none after PR #1162
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The next direct action is to exploit every zero-excess parameter fiber of
the two `A=1` pair-boundary biforms, including positive-padding fibers.
