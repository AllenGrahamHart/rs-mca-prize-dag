# Dependency sub-DAG

```text
l1_mersenne_next_to_maximal_hypergeometric_normal_form [PROVED]
       |
       +--> l1_mersenne_hnf_order_zero_quadratic_collision_router [PROVED]
       |
       +--> l1_mersenne_hnf_m8_order_zero_quadratic_exclusion [PROVED]
       |
       +--> l1_mersenne_hnf_m16_order_zero_single_collision_exclusion [PROVED]
                              |
                              v
l1_mersenne_hnf_m16_order_zero_even_quadratic_exclusion [PROVED]
                              |
                              v  (evidence)
                    l1_mixed_petal_amplification [TARGET]
```

The collision router identifies the only remaining multiplicity shape; the
two row-specific exclusions remove every other quadratic shape. This node
deletes the final even shape and therefore closes degree two, not the full
order-zero chamber.
