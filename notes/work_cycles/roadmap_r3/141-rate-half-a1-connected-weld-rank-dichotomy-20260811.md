# Cycle 141: rate-half `A=1` connected weld-rank dichotomy (2026-08-11)

## Connected complement graph

For both pair boundaries, any two selected zero-excess fibers share a
nonincident classified row:

```text
extremal margin: p+3+d_A,
strict margin:   4+r_A.
```

Every classified row also misses a selected fiber, with margins `e+2` and
`(e+5)/2`. The complement incidence graph is therefore connected. Its sparse
weld matrix has only two possible ranks:

```text
rank W=R:   boundary excluded immediately;
rank W=R-1: one unique projective full-support scalar vector remains.
```

In the second case, common-biform realizability is exactly the test
`Krow lambda=0`; no full-support search remains.

## Calibration

At `e=7,d_A=1`, the smooth cyclic `28 x 21` ledger has weld rank `28` over
both `F_337` and `F_421`. One hundred deterministic degree-preserving switch
trials per field also all had rank `28`. This calibrates the exclusion but is
not an exhaustive or official-row proof.

## Burn-down

```text
result:                  PROVED connected weld-rank dichotomy
DAG delta:               +1 PROVED
DAG after compile:       2293 nodes, 6738 edges
critical status delta:   none; 28 every-route TARGETs remain
probe:                   202/202 profiles full weld rank; evidence only
delta-star movement:     none
new assumptions:         none
compute requests:        none
```

The route-deciding residue is now whether any allowed profile can make the
weld cycles consistent. A survivor has one forced scalar vector and must
then pass `Krow` and the retained Hankel/source identities.
