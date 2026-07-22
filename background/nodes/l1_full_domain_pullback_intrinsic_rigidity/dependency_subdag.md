# Dependency sub-DAG: L1 full-domain pullback intrinsic rigidity

```text
l1_general_pullback_interleaving_descent [PROVED] ----------req----+
pma_exact_periodic_owner [PROVED] --------------------------req----+
                                                                    v
l1_full_domain_pullback_intrinsic_rigidity [PROVED]
    --ev--> l1_full_pullback_divisibility_johnson_closure [PROVED]
    --ev--> l1_mixed_residual_intersection_pin [PROVED]
    --ev--> l1_mixed_petal_amplification [TARGET]
    --ev--> petal_mixed_amplification [CONDITIONAL]
```

The Johnson node remains a valid direct estimate, but its full-partition
sub-Johnson residual is superseded by intrinsic ownership.
