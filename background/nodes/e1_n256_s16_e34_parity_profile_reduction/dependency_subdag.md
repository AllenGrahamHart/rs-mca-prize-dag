# Dependency sub-DAG

```text
e1_n256_s16_e34_three_profile_reduction [PROVED] --req-->
e1_n256_s16_e34_parity_profile_reduction [PROVED]

e1_n256_s16_signed_chord_collision_gate [PROVED] --req-->
e1_n256_s16_e34_parity_profile_reduction [PROVED]

e1_n256_s16_e34_parity_profile_reduction [PROVED] --ev-->
e1_official_prime_exception_control [TARGET]

e1_n256_s16_e34_parity_profile_reduction [PROVED] --ev-->
unsafe_crossing_family_instantiation [TARGET]
```

The node removes two exact profiles and adds a light-support Sidon constraint.
It is evidence for the universal targets until a complete collision exclusion
or distinct-value transport theorem is supplied.
