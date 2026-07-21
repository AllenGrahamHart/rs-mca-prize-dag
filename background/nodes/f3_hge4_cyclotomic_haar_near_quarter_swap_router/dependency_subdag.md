# Dependency sub-DAG

```text
f3_hge4_exact_ratio_tower_orbit_compiler (PROVED)
                         \
                          -> f3_hge4_cyclotomic_haar_near_quarter_swap_router
                         /                                      (PROVED)
f3_hge4_primitive_swap_odd_moment_router (PROVED)                 |
                                                                    ev
                                                                     v
                                             f3_hge4_norm_gate_count (TARGET)
```

The new node eliminates the free class in an explicit growing band. It uses
the existing swap theorem only after proving that the antipode exchanges the
two supports. The odd swap count remains part of the HGE4 target.
