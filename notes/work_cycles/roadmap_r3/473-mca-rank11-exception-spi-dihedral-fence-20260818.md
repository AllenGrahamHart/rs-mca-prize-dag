# Cycle 473: dihedral exception-SPI fence

## Starting pins

```text
our SHA: 595e19952
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream factor-synchronization tip: #1173 at 2788d5ec3
upstream split-pencil tip: #1170 at d296510e80
```

## Result: PROVED route fence

Let `N` be a power of two, `d in {1,2,4}`, and `M=N/d`. For a nonsquare
`a in mu_M`, inversion `z -> a/z` partitions `mu_M` into `M/2` pairs.
The pencil

```text
u=X^(2d)+a,       v=X^d
```

has one split degree-`2d` fiber

```text
u-(z+a/z)v=(X^d-z)(X^d-a/z)
```

for every pair. Distinct pairs give distinct slopes and disjoint root sets.
At `N=2^21`, the exact counts are `1048576`, `524288`, and `262144` for
degrees `2`, `4`, and `8`.

This complements the cyclic power-map fence. The abstract endpoint therefore
has the full cyclic/dihedral pullback boundary anticipated by the existing
Luroth taxonomy, but the available many-fiber theorem triggers only at
`N^(2/3)` scale and cannot classify a packet of twenty fibers.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +2 edges
critical status delta: none
route delta: power-only classification falsified; cyclic/dihedral boundary pinned
new assumptions: none
next action: exploit heavy-ruling semantics or prove a twenty-fiber bounded-degree primitive cap
```

## Nonclaims

- no received pair, rational certificate, or heavy-ruling lift is constructed;
- no MCA counterexample or rational payment;
- no adjacent-row safety or prize closure.

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_exception_spi_dihedral_quotient_fence/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_exception_spi_dihedral_quotient_fence/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_exception_spi_dihedral_quotient_fence/verify_audit.py
```
