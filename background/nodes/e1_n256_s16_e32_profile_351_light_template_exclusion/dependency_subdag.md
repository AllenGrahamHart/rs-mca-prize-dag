# Dependency sub-DAG

```text
e1_n256_s16_e32_profile_parity_diameter_reduction (PROVED)
                         |
                         +-------------------+
                                             v
e1_n256_s16_e32_four_odd_light_template_reduction (PROVED)
                                             |
collision_norm_criterion (PROVED) -----------+
                                             v
e1_n256_s16_e32_profile_351_light_template_exclusion (PROVED)
                         |
                         +---- ev ----> e1_official_prime_exception_control
                         +---- ev ----> unsafe_crossing_family_instantiation
```

The node removes only profile `(3,5,1)`. Profile `(4,7)` remains the sole
`V=64` branch and is not a dependency of this claim.
