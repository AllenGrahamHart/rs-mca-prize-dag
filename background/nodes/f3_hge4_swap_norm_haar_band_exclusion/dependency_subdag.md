# Dependency sub-DAG

```text
f3_hge4_primitive_swap_odd_moment_router (PROVED)
                         \
                          -> f3_hge4_swap_norm_haar_band_exclusion (PROVED)
                         /                                      |
f3_hge4_cyclotomic_haar_near_quarter_swap_router (PROVED)       ev
                                                                 v
                                          f3_hge4_norm_gate_count (TARGET)
```

The first dependency supplies the exact odd-moment swap equations. The second
supplies the all-pairs-to-swap implication in the narrower Haar band. Their
combination makes that narrower band completely empty.
