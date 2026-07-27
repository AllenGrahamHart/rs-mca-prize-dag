# Dependency sub-DAG

```text
e1_n256_s16_e28_profile_parity_light_reduction (PROVED) --+
                                                           +--> E28 endpoint exclusion
e1_n256_s16_e28_eight_profile_joint_exclusion (PROVED) ----+    (PROVED)
```

The endpoint node is only the exhaustive synthesis. All computation remains
in its exclusion dependency. It supplies evidence to both E1 consumers.
