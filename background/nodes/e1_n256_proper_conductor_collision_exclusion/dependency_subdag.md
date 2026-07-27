# Dependency sub-DAG

```text
collision_norm_criterion [PROVED] --------------------+
                                                       +--req-->
e1_prime_field_l2_norm_collision_radius [PROVED] -----+
    e1_n256_proper_conductor_collision_exclusion [PROVED]

e1_n256_proper_conductor_collision_exclusion [PROVED]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

This removes all proper cyclotomic-subfield lifts from both first-band
profiles. It is evidence for, not a requirement of, the route-wide target.
