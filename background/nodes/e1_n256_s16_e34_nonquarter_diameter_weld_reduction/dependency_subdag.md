# Dependency sub-DAG

```text
e1_n256_s16_e34_heavy_chord_template_reduction [PROVED] --req-->
e1_n256_s16_e34_nonquarter_diameter_weld_reduction [PROVED]

e1_n256_s16_e34_parity_profile_reduction [PROVED] --req-->
e1_n256_s16_e34_nonquarter_diameter_weld_reduction [PROVED]

e1_n256_s16_e34_nonquarter_diameter_weld_reduction [PROVED] --ev-->
e1_official_prime_exception_control [TARGET]

e1_n256_s16_e34_nonquarter_diameter_weld_reduction [PROVED] --ev-->
unsafe_crossing_family_instantiation [TARGET]
```

The node is a finite normal-form reduction. It remains evidence until the
complete chamber is excluded or a stronger analytic argument consumes it.
