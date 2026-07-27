# Dependency sub-DAG

```text
e1_n256_s16_e34_parity_profile_reduction [PROVED] --req-->
e1_n256_s16_e34_heavy_chord_template_reduction [PROVED]

e1_n256_s16_signed_chord_collision_gate [PROVED] --req-->
e1_n256_s16_e34_heavy_chord_template_reduction [PROVED]

e1_n256_s16_e34_heavy_chord_template_reduction [PROVED] --ev-->
e1_official_prime_exception_control [TARGET]

e1_n256_s16_e34_heavy_chord_template_reduction [PROVED] --ev-->
unsafe_crossing_family_instantiation [TARGET]
```

The node turns an opaque repeated-chord condition into four explicit additive
templates. It remains evidence until every template is excluded or paid.
