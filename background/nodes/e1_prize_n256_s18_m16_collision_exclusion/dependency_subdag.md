# Dependency sub-DAG

```text
e1_prize_n256_s18_m16_high_variance_exclusion [PROVED]
    --req--> e1_prize_n256_s18_m16_collision_exclusion [PROVED]

e1_prize_n256_s18_m16_collision_exclusion [PROVED]
    --ev--> e1_official_low_square_mass_pair_budget [TARGET]
    --ev--> e1_official_prime_exception_control [TARGET]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

The outgoing edges remain evidence-only because cofactors `2,4` and the
aggregate weighted edge count remain open.
