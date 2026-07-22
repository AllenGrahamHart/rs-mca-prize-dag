# Dependency sub-DAG: L1 maximal background-anchor injection

```text
l1_core_defect_reduction [PROVED]
    --req--> l1_maximal_background_anchor_injection [PROVED]
                  |--ev--> l1_mixed_residual_intersection_pin [PROVED]
                  |--ev--> l1_mixed_petal_amplification [TARGET]
                  `--ev--> petal_mixed_amplification [TARGET]
```

The required edge supplies the exact `(F,W)` normal form. The outgoing edges
are evidence: the injection strengthens the payment ledger but does not sum
the remaining strata or close either target.
