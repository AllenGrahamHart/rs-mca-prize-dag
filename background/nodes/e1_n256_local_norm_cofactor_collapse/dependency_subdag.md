# Dependency sub-DAG

```text
e1_pair_feasible_prime_field_reduction [PROVED] ------+
                                                       +--req-->
e1_n256_2adic_cofactor_collision_exclusion [PROVED] --+
    e1_n256_local_norm_cofactor_collapse [PROVED]

e1_n256_local_norm_cofactor_collapse [PROVED]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

This converts norm magnitude and valuation into exact finite cofactor
interfaces. It does not pay any resulting odd norm.
