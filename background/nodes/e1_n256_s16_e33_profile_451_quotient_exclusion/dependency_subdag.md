# Dependency sub-DAG

```text
e1_n256_s16_e33_profile_parity_diameter_reduction [PROVED] --req-->
e1_n256_s16_e33_profile_451_quotient_exclusion [PROVED]

e1_n256_proper_conductor_collision_exclusion [PROVED] --req-->
e1_n256_s16_e33_profile_451_quotient_exclusion [PROVED]

collision_norm_criterion [PROVED] --req-->
e1_n256_s16_e33_profile_451_quotient_exclusion [PROVED]

e1_n256_s16_e33_profile_451_quotient_exclusion [PROVED] --ev-->
e1_official_prime_exception_control [TARGET]

e1_n256_s16_e33_profile_451_quotient_exclusion [PROVED] --ev-->
unsafe_crossing_family_instantiation [TARGET]
```

Two V=66 profiles remain, so the consumer edges are evidence edges.
