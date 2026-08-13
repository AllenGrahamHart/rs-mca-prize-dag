# Cycle 268: rate-half Shape-A tensor-rank-three upstream export (2026-08-13)

Cycle 267 was exported to the existing Lane-T draft PR `#1161` as Section
46. The export preserves the exact scope:

```text
official tensor rank <=2:       PROVED impossible (Section 45)
official tensor rank =3:        PROVED four-row frame router
triple incidences in the frame: PROVED impossible
official repeated-slope floor:  183251937955
official one-pair floor:         30541989660
rank-three frame exclusion:      OPEN
tensor rank >=4:                 OPEN
```

The compact verifier now replays the all-partition evidence, exact
degree-ledger fence, rank-two exclusion arithmetic, and rank-three frame
arithmetic together. It pins seventeen source assets at the new local
source commit.

```text
local source:            2871b3bdd2b5b2d5161cbb57b204b8b920faa67c
upstream PR:             #1161 (draft)
upstream commit:         cf235bf
upstream section:        46
review comment:          issuecomment-5282481664
compact replay:          630 cases + exact rank-27 fence + frame floors
source pins:             17/17
compact mutations:       7/7 normal and optimized
main replay:             39074 checks, 144/144 source pins
main mutations:          118/118 normal and optimized
row/endpoint movement:   none claimed
```

The next route action is to combine the triple-free four-row frame with the
actual Shape-A source, spread, or collision semantics. A bare pair-overlap
count is not a payment because its `~e/6` floor is below the generic
two-row average scale.
