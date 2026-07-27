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
l1_mersenne_hnf_m16_order_zero_single_collision_exclusion [PROVED]
                       |
                       v  (evidence)
             l1_mixed_petal_amplification [TARGET]
```

The collision-free theorem forces at least one repeat. This theorem removes
exactly one; the router makes every remaining multiple-repeat quadratic even
with antipodal collision pairs. The parallel proved
`l1_mersenne_hnf_m8_order_zero_quadratic_exclusion` supplies the `m=8`
part of the global degree-two frontier.
