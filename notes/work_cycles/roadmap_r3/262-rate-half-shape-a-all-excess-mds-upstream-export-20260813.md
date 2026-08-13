# Cycle 262: rate-half Shape-A all-excess MDS upstream export (2026-08-13)

Cycle 261's all-fiber compatibility gate was exported to the existing
Lane-T packet in `przchojecki/rs-mca` draft PR `#1161`.

Upstream Section 44 records the exact matrix

```text
(K_all)_((i,l),(delta,h))
 =d_(delta,i-h)delta^l/L_Gamma'(delta)
```

and proves that its kernel is exactly the residual-fiber data interpolating
to one biform. The Shape-A excess sum reduces the matrix to exactly `4e`
columns. Unlike a bound on degree drops alone, excluding a block-supported
kernel of this matrix would exclude the entire surviving Shape-A biform.

```text
local source:            2b13f71b0d67a36dc5e810e3a0f867586912c473
upstream PR:             #1161 (draft)
upstream commit:         ed1d5b1
upstream section:        44
exact checks:            39074
source pins:             144/144
hostile field mutations: 118/118 normal and optimized
small analogue:          102/102 profiles full rank in two fields
row/endpoint movement:   none claimed
next route action:       prove no block-supported kernel or classify every
                         exceptional incidence profile
```
