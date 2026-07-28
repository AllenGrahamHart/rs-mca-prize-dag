# Dependency sub-DAG

```text
collision_norm_criterion [PROVED] ---------------------+
e1_prize_field_floor_even_norm_exclusion [PROVED] -----+--req-->
e1_n256_local_norm_cofactor_collapse [PROVED] ----------+
    e1_prize_n256_s18_variance_cofactor_windows [PROVED]

e1_prize_n256_s18_variance_cofactor_windows [PROVED]
    --req--> e1_prize_n256_s18_m1028_collision_exclusion [PROVED]
    --req--> e1_prize_n256_s18_m514_collision_exclusion [PROVED]
    --req--> e1_prize_n256_s18_m256_collision_exclusion [PROVED]
    --req--> e1_prize_n256_s18_m16_high_variance_exclusion [PROVED]
    --ev--> e1_official_low_square_mass_pair_budget [TARGET]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

The node eliminates one of seven prize cofactors and narrows the other six;
proved children remove three more cofactors and the high `m=16` chambers.
All TARGET consumer edges are evidence-only because residual cofactors and
the aggregate weighted count remain open.
