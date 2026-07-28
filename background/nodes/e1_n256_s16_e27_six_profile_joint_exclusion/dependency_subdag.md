# Dependency sub-DAG

```text
e1_n256_s16_e27_profile_parity_light_reduction (PROVED) --+
e1_n256_proper_conductor_collision_exclusion (PROVED) -----+--> E27 six-profile
collision_norm_criterion (PROVED) -------------------------+    joint exclusion
                                                                   |
                                                                   +--> E27 endpoint
```

The two census engines share only the input atlas and output contract. The
folded update and direct negacyclic multiplication are independent.
