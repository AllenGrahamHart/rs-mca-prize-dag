# Dependency sub-DAG

```text
e1_n256_s16_e34_three_profile_reduction [PROVED] --req-->
e1_n256_s16_e34_endpoint_exclusion [PROVED]

e1_n256_s16_e34_parity_profile_reduction [PROVED] --req-->
e1_n256_s16_e34_endpoint_exclusion [PROVED]

e1_n256_s16_e34_heavy_chord_template_reduction [PROVED] --req-->
e1_n256_s16_e34_endpoint_exclusion [PROVED]

e1_n256_s16_e34_quarter_template_exclusion [PROVED] --req-->
e1_n256_s16_e34_endpoint_exclusion [PROVED]

e1_n256_s16_e34_nonquarter_diameter_template_exclusion [PROVED] --req-->
e1_n256_s16_e34_endpoint_exclusion [PROVED]

e1_n256_s16_e34_progression_template_exclusion [PROVED] --req-->
e1_n256_s16_e34_endpoint_exclusion [PROVED]

e1_n256_s16_e34_generic_template_exclusion [PROVED] --req-->
e1_n256_s16_e34_endpoint_exclusion [PROVED]

e1_n256_s16_e34_endpoint_exclusion [PROVED] --ev-->
e1_official_prime_exception_control [TARGET]

e1_n256_s16_e34_endpoint_exclusion [PROVED] --ev-->
unsafe_crossing_family_instantiation [TARGET]
```

The endpoint is closed, but lower positive even variances keep the universal
targets open.
