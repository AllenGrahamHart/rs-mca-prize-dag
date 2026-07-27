# Dependency sub-DAG

```text
e1_n256_s16_e32_profile_parity_diameter_reduction [PROVED] --req-->
e1_n256_s16_e32_profile_08_light_template_exclusion [PROVED]

e1_n256_s16_e32_profile_08_light_template_exclusion [PROVED] --ev-->
e1_official_prime_exception_control [TARGET]

e1_n256_s16_e32_profile_08_light_template_exclusion [PROVED] --ev-->
unsafe_crossing_family_instantiation [TARGET]
```

This closes one of the three `V=64` profiles. The other two branches remain,
so both consumer edges are evidence edges.
