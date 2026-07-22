# Dependency sub-DAG

```text
f3_hge4_exact_ratio_tower_orbit_compiler [PROVED] ----req---+
                                                            |
f3_hge4_ambient_norm_level_contraction [PROVED] ------req---+
                                                            v
f3_hge4_multiscale_haar_m64_level_close [PROVED] ------ev-->
                                     f3_hge4_norm_gate_count [TARGET]
```

The ambient dependency already carries the quarter-width,
complement-third, Vandermonde, and swap-norm packets. The new node supplies
the shared multiscale energy identity and the two missing `m=64` endpoints.
