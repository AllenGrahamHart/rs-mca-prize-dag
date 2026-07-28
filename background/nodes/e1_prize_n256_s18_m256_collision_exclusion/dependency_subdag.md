# Dependency sub-DAG

```text
e1_prize_n256_s18_variance_cofactor_windows [PROVED]
    --req--> e1_prize_n256_s18_m256_collision_exclusion [PROVED]

e1_prize_n256_s18_m256_collision_exclusion [PROVED]
    --ev--> e1_official_low_square_mass_pair_budget [TARGET]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

The theorem removes one leading-profile prize cofactor. All consumer edges
remain evidence-only because three cofactor classes and later profiles survive.
