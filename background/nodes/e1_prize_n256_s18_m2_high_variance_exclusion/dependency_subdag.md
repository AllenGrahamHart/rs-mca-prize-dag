# Dependency sub-DAG

```text
e1_prize_n256_s18_variance_cofactor_windows [PROVED]
    --req--> e1_prize_n256_s18_m2_high_variance_exclusion [PROVED]

e1_prize_n256_s18_m2_high_variance_exclusion [PROVED]
    --req--> e1_prize_n256_s18_m2_collision_exclusion [PROVED]
    --ev--> e1_official_low_square_mass_pair_budget [TARGET]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

The outgoing target edges remain evidence-only because later profiles and the
aggregate weighted pair budget remain open.
