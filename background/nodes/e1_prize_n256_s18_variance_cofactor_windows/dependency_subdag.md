# Dependency sub-DAG

```text
collision_norm_criterion [PROVED] ---------------------+
e1_prize_field_floor_even_norm_exclusion [PROVED] -----+--req-->
e1_n256_local_norm_cofactor_collapse [PROVED] ----------+
    e1_prize_n256_s18_variance_cofactor_windows [PROVED]

e1_prize_n256_s18_variance_cofactor_windows [PROVED]
    --ev--> e1_official_low_square_mass_pair_budget [TARGET]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

The node eliminates one of seven prize cofactors and narrows the other six.
All consumer edges are evidence-only because the residual vectors have not
been counted or excluded.
