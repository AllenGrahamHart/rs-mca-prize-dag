# Dependency sub-DAG - L1 polarized petal-entropy ledger

```text
pma_petal_pattern_root_pinning_ledger [PROVED]
                    |
                    +--req--> l1_polarized_petal_entropy_ledger [PROVED]
                                      |
                                      +--req--> l1_mixed_residual_intersection_pin [PROVED]
                                      +--ev----> l1_mixed_petal_amplification [TARGET]
                                      +--ev----> petal_mixed_amplification [TARGET]
```

The new ledger strengthens an aggregate over an already-proved exact-pattern
injection. It introduces no open child.
