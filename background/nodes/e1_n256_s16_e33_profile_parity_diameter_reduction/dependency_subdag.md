# Dependency sub-DAG

```text
e1_n256_s16_e34_endpoint_exclusion [PROVED] --req-->
e1_n256_s16_e33_profile_parity_diameter_reduction [PROVED]

e1_n256_s16_sparse_l1_variance_exclusion [PROVED] --req-->
e1_n256_s16_e33_profile_parity_diameter_reduction [PROVED]

e1_n256_s16_signed_chord_collision_gate [PROVED] --req-->
e1_n256_s16_e33_profile_parity_diameter_reduction [PROVED]

collision_norm_criterion [PROVED] --req-->
e1_n256_s16_e33_profile_parity_diameter_reduction [PROVED]

e1_n256_s16_e33_profile_parity_diameter_reduction [PROVED] --ev-->
e1_official_prime_exception_control [TARGET]

e1_n256_s16_e33_profile_parity_diameter_reduction [PROVED] --ev-->
unsafe_crossing_family_instantiation [TARGET]
```

The node narrows the next endpoint but does not close any of its four
profiles, so both consumer edges remain evidence edges.
