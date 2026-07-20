# Dependency sub-DAG: L1 fixed-support cross-determinant fiber bound

```text
l1_bounded_mark_affine_split_pencil_compiler [PROVED] --------req----+
l1_affine_split_pencil_cross_determinant_uniqueness [PROVED] -req----+
pma_saturated_mixed_support_kernel [PROVED] ------------------req----+
                                                                       v
l1_fixed_support_cross_determinant_fiber_bound [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```
