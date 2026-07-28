# Dependency sub-DAG

```text
e1_n256_s16_e25_profile_parity_light_reduction (PROVED) --+
e1_n256_proper_conductor_collision_exclusion (PROVED) -----+--> E25 nine-profile
collision_norm_criterion (PROVED) -------------------------+    exclusion
                                                                   |
                                                                   +--> E25 endpoint
```

The census engines share only the input atlas and output contract. Their
folded-chord and direct-negacyclic profile computations are independent.
