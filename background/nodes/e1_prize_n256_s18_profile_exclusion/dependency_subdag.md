# Dependency sub-DAG

```text
e1_low_square_mass_weighted_kernel_dictionary ------------+
e1_prize_n256_s18_variance_cofactor_windows --------------+
e1_prize_n256_s18_m1028_collision_exclusion --------------+
e1_prize_n256_s18_m514_collision_exclusion ---------------+
e1_prize_n256_s18_m256_collision_exclusion ---------------+--req-->
e1_prize_n256_s18_m16_collision_exclusion ----------------+
e1_prize_n256_s18_m4_collision_exclusion -----------------+
e1_prize_n256_s18_m2_collision_exclusion -----------------+
    e1_prize_n256_s18_profile_exclusion [PROVED]

e1_prize_n256_s18_profile_exclusion
    --ev--> e1_official_low_square_mass_pair_budget [TARGET]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

The target edges remain evidence-only because other profiles, RowC, and later
square-mass bands remain open.
