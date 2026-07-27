# Dependency sub-DAG

```text
l1_mersenne_next_to_maximal_hypergeometric_normal_form [PROVED]
       |                              |
       v                              v
l1_mersenne_hnf_order_zero_     l1_mersenne_hnf_order_zero_
quadratic_collision_router      quadratic_collisionfree_exclusion
       |                              |
       +---------------+--------------+
                       v
l1_mersenne_hnf_m8_order_zero_quadratic_exclusion [PROVED]
                       |
                       v  (evidence)
             l1_mixed_petal_amplification [TARGET]
```

The two quadratic dependencies reduce the `m=8` multiplicity partition to
exactly one repeated color. This node then removes that final partition by a
centered-moment and constant-coefficient torsion certificate.
