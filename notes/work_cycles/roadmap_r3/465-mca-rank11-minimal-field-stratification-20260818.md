# Cycle 465: rank-eleven minimal-field stratification fence

## Starting pins

```text
our SHA: 6eed7ef72
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
upstream open PRs: #1161..#1173; selected split-pencil tip #1170 at d296510e80
upstream rich-flat tip: #1173 at 2788d5ec3
```

## Result: PROVED field split and automatic-descent fence

For every used factor in the heavy Segre bucket, the projective coefficient
ratios of `(P,Q,[g])` define a unique minimal field over the domain-generated
base field. Since the official extension degree is six, the possible
relative degrees are exactly

```text
1, 2, 3, 6.
```

The `9965407986` retained slopes therefore contain one degree stratum of
mass at least

```text
ceil(9965407986/4)=2491351997.
```

The fixed-factor cap `248644099` then forces at least 11 projective factors
in that stratum, with strict gap

```text
2491351997-10*248644099=4911007.
```

A symbolic packet over `F_(p^6)` with

```text
P=<1,X^2+alpha X>, Q=<1,X^4>, K=7
```

has base-free factors, product rank four, and 41 used ruling planes, but is
not Frobenius-stable over `F_p`. Thus field-internal Segre data and the
factor cap do not force base descent. The packet is an algebraic route fence,
not an MCA counterexample.

## Burn-down

```text
critical target attacked: rate_half_band_crossing_location
DAG delta: +1 background PROVED node, +3 edges
critical status delta: none
route delta: vague base-descent ask -> degree-1 census branch / degree-2,3,6 transfer branch
new assumptions: none
next action: prove a shared-owner Galois-orbit transfer, or bind the degree-one stratum to one fixed upstream selected-support owner
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_minimal_field_stratification_fence/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_minimal_field_stratification_fence/verify.py --tamper-selftest
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_heavy_plane_minimal_field_stratification_fence/verify_audit.py
```
