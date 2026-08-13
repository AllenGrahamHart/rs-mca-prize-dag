# Cycle 266: rate-half Shape-A low-rank fence upstream export (2026-08-13)

Cycles 263--265 were exported to the existing Lane-T draft PR `#1161` as
Section 45. The upstream packet records all three status levels separately:

```text
all-partition e=7 scan:       EXPERIMENTAL evidence, 630/630 full rank
degree-ledger universal rank: REFUTED by exact rank-27 F_211 kernel
official tensor rank <=2:     PROVED impossible
```

The implementation uses a separate verifier rather than extending the
already-large main experiment code with another numerical engine. The main
verifier retains the complete theorem replay and refreshed source pin.

```text
local source:            2d376a7e2061b0adc214e071c01dd270c0f2421c
upstream PR:             #1161 (draft)
upstream commit:         f011891
upstream section:        45
review comment:          issuecomment-5282276863
new replay:              630 partition cases + exact rank-27 kernel
new hostile mutations:   5/5 normal and optimized
main replay:             39074 checks, 144/144 source pins
main hostile mutations:  118/118 normal and optimized
row/endpoint movement:   none claimed
```

The next route action is no longer universal degree-ledger rank. It is to
classify or exclude tensor-rank-at-least-three `K_all` kernels using spread,
collision, or common source/Hankel structure.
