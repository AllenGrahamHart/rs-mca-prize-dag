# Dependency sub-DAG

```text
e1_n256_s16_high_variance_collision_exclusion [PROVED] --+
                                                         +--req-->
collision_norm_criterion [PROVED] -----------------------+
    e1_n256_s16_sparse_l1_variance_exclusion [PROVED]

e1_n256_s16_sparse_l1_variance_exclusion [PROVED]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

This is an analytic child of the former `V<=134` residual. It leaves
a smaller positive even `V<=82` leaf.
