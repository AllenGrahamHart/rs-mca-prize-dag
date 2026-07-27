# Dependency sub-DAG

```text
collision_norm_criterion [PROVED] --------------------+
                                                       +--req-->
e1_prime_field_l2_norm_collision_radius [PROVED] -----+
    e1_n256_2adic_cofactor_collision_exclusion [PROVED]

e1_n256_2adic_cofactor_collision_exclusion [PROVED]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

This is an independent necessary-condition gate on both first-band profiles.
It is route evidence and does not become a requirement of the open target.
