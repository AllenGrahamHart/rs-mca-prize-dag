# Cycle 274: rate-half Shape-A domain birationality upstream export (2026-08-13)

Cycle 273 was exported to the existing Lane-T draft PR `#1161` as Section
49. It completes the symmetric birationality packet:

```text
parameter coefficient map degree: 1
domain coefficient map degree:    1
tensor-rank scope:                every minimal r>=2
repeated values:                  singular branches only
row/endpoint movement:            none
```

```text
local source:            f8d4459a54e8df7ac69b7abcd39716da69c20199
upstream PR:             #1161 (draft)
upstream commit:         8f83b95
upstream section:        49
review comment:          issuecomment-5283302727
compact replay:          630 cases + rank fence + both birationality ledgers
source pins:             32/32
compact mutations:       15/15 normal and optimized
```

The next route action is no longer to classify many-to-one coefficient
covers. It is to bound singular branch aggregation on the two birational
images, or couple their common incidence divisor to source/Hankel and
scalar-weld data.
