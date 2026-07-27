# Dependency sub-DAG

```text
e1_n256_s16_e34_generic_affine_weld_reduction [PROVED] --req-->
e1_n256_s16_e34_generic_template_exclusion [PROVED]

e1_n256_proper_conductor_collision_exclusion [PROVED] --req-->
e1_n256_s16_e34_generic_template_exclusion [PROVED]

e1_n256_s16_e34_three_profile_reduction [PROVED] --req-->
e1_n256_s16_e34_generic_template_exclusion [PROVED]

collision_norm_criterion [PROVED] --req-->
e1_n256_s16_e34_generic_template_exclusion [PROVED]

e1_n256_s16_e34_generic_template_exclusion [PROVED] --ev-->
e1_official_prime_exception_control [TARGET]

e1_n256_s16_e34_generic_template_exclusion [PROVED] --ev-->
unsafe_crossing_family_instantiation [TARGET]
```

This closes the fourth and final heavy template at E34. The endpoint synthesis
still records the complete profile-to-template chain explicitly.
