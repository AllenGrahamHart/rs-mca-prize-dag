# Cycle 278: rate-half Shape-A source-rank amplification upstream export (2026-08-13)

Cycle 277 was exported to the existing Lane-T draft PR `#1161` as Section
51. The export explicitly distinguishes the first-degree primitive-kernel
parameter `e` from the earlier maximal-component parameter and records the
result as a macroscopic rank floor, not a Shape-A closure.

```text
local source:            b7e0ab6e45b6d304b13efa4442ecd2fd7a3ea350
upstream PR:             #1161 (draft)
upstream commit:         3abd608
upstream section:        51
review comment:          issuecomment-5283775237
compact replay:          630 cases + all geometry/rank ledgers
source pins:             42/42
compact mutations:       21/21
proved rank floor:       61083979322
row/endpoint movement:   none
```

The next Shape-A action should use the exact three-quadratic generation of
the full degree-`e` parameter space and the source-Hankel isotropy at
macroscopic rank. Low-rank projective casework is now retired.
