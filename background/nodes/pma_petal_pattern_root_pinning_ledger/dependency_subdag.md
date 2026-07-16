# Dependency sub-DAG - PMA petal-pattern root-pinning ledger

```text
pma_saturated_mixed_support_kernel [PROVED] ---------\
                                                        -> pma_petal_pattern_root_pinning_ledger [PROVED]
petal_reserve_rich_fiber_reduction [PROVED] --------/                         |
                                                                                 +--ev--> petal_mixed_amplification [TARGET]
                                                                                 +--ev--> imgfib [CONDITIONAL]
```

The first dependency supplies saturation, maximal rank, and root pinning. The
second supplies the maximal-source agreement inequalities used to prove
`h>d`. The new theorem closes the bounded `u+e` aggregate region and leaves a
strictly narrower direct residual; it is not a conditional leaf.
