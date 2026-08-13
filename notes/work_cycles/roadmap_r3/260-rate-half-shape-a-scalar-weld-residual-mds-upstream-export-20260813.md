# Cycle 260: rate-half Shape-A scalar-weld residual-MDS upstream export (2026-08-13)

Cycle 259's exact scalar-weld residual flag was exported to the existing
Lane-T packet in `przchojecki/rs-mca` draft PR `#1161`.

Upstream Section 43 records that every fiber degree drop is the exact
initial zero run of support-dependent residual-RS parity rows applied to
the same projective weld vector:

```text
j_delta=3e+r_delta-1,
q_delta=initial zero-run length of
        K_(delta,0)lambda,K_(delta,1)lambda,...,
deg T=e-sum_delta q_delta.
```

This is the first formulation of the remaining Shape-A norm problem that
retains the global common-biform coupling while removing every independent
per-fiber residual choice. The export claims no rank bound.

```text
local source:            dadd5edf528b6787cfdf846e93e696de191c0c77
upstream PR:             #1161 (draft)
upstream commit:         0667365
upstream section:        43
exact checks:            38938
source pins:             134/134
hostile field mutations: 112/112 normal and optimized
row/endpoint movement:   none claimed
next route action:       bound dependencies among the stacked parity rows
                         on the unique scalar-weld vector
```
