# Cycle 256: rate-half shape-A bordered-Hankel upstream export (2026-08-13)

Cycle 255's proved determinantal presentation was exported to the existing
Lane-T packet in `przchojecki/rs-mca` draft PR `#1161`.

The upstream Section 41 records both exact forms of every omitted defect:

```text
det M[k<-v_s]=D_1 q_k R_(d+1+s),
B_s=det widehat M_s=-D_1 R_(d+1+s)^2,
```

where `B_s` is also the generalized-alternant Cauchy--Binet source sum over
subsets of size `d+2`. It then splits the full off-line flag into

```text
padding flag: deg=e-7=183251937956,
regular flag: deg=2e+7=366503875933.
```

At a regular root, a degree-drop run is exactly stagnation of the bordered
Hankel column rank. The export explicitly preserves the two remaining proof
obligations and does not infer a payment from the determinant squares.

```text
local source:            1e08388888ab2457d8f1e2bcb8de5afd1464ff80
upstream PR:             #1161 (draft)
upstream commit:         208bf53
upstream section:        41
exact checks:            38204
source pins:             114/114
source subset terms:     252/252
hostile field mutations: 101/101 normal and optimized
row/endpoint movement:   none claimed
next route action:       control the padding flag or prove regular
                         bordered-source rank non-stagnation
```
