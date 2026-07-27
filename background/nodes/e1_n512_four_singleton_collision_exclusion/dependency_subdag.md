# Dependency sub-DAG

```text
collision_norm_criterion [PROVED] --------------------+
                                                       +--req-->
e1_prime_field_l2_norm_collision_radius [PROVED] -----+
    e1_n512_four_singleton_collision_exclusion [PROVED]

e1_n512_four_singleton_collision_exclusion [PROVED]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

The theorem closes one of the two profiles in the first surviving `N=512`
band. It is evidence for, not a requirement of, the route-wide pointwise
collision target.
