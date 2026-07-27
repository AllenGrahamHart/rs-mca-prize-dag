# Dependency sub-DAG

```text
collision_norm_criterion [PROVED] --------------------+
                                                       +--req-->
e1_prime_field_l2_norm_collision_radius [PROVED] -----+
    e1_n256_s16_high_variance_collision_exclusion [PROVED]

e1_n256_s16_high_variance_collision_exclusion [PROVED]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

This narrows one first-band profile to a bounded low-variance residual. It is
evidence for, not a requirement of, the route-wide collision target.
