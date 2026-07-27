# Dependency sub-DAG

```text
collision_norm_criterion [PROVED] --------------------+
                                                       +--req-->
e1_pair_feasible_prime_field_reduction [PROVED] ------+
    e1_prime_field_l2_norm_collision_radius [PROVED]

e1_prime_field_l2_norm_collision_radius [PROVED]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

This closes only the first swap-distance bands. It is evidence for, not a
requirement of, the open pointwise collision target.
