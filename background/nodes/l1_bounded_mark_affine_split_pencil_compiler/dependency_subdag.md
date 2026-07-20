# Dependency sub-DAG: L1 bounded-mark affine split-pencil compiler

```text
l1_polarized_petal_entropy_ledger [PROVED] ----------------req----+
l1_bounded_polarity_marked_full_pencil_reduction [PROVED] -req----+
pma_saturated_mixed_support_kernel [PROVED] ---------------req----+
                                                                   v
l1_bounded_mark_affine_split_pencil_compiler [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```
