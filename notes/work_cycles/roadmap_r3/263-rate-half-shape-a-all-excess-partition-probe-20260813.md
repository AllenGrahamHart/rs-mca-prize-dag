# Cycle 263: rate-half Shape-A all-excess partition probe (2026-08-13)

The first `e=7` calibration used the spread profile with fourteen
zero-excess and seven excess-one slopes. To test whether that profile hid a
partition-specific rank failure, the all-excess gate was scanned across all
fifteen integer partitions of the total excess `7`.

For each partition the probe constructs one incidence table with the exact
row and column degrees and twenty degree-preserving switches. It repeats the
scan over `F_337` and `F_421`. All `630` matrices have full column rank:

```text
profiles:                 15/15 excess partitions
cases:                    630 deterministic realizations
minimum rank:             28/28
deficient cases:          none
compute:                  2.5 seconds guarded local exact arithmetic
status effect:            none; evidence only
critical status effect:   none
```

The result removes excess-partition sampling bias from the small analogue.
It does not enumerate incidence tables, model the official positive padding,
or prove absence of a block-supported kernel. The next route action remains
an analytic use of the three-center support/source structure, or a
classification of exceptional `K_all` kernels.
