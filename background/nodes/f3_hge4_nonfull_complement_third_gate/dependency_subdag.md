# Dependency sub-DAG

```text
f3_hge4_exact_ratio_tower_orbit_compiler [PROVED] --------req--+
                                                               |
f3_hge4_primitive_shift_pair_near_square_union_router [PROVED]-+
                                                               |
                                                               v
                  f3_hge4_nonfull_complement_third_gate [PROVED]
                                                               |
                                                              ev
                                                               |
                                                               v
                         f3_hge4_norm_gate_count [TARGET]
```

The theorem deletes the upper third of every exact-level width range. The
remaining exact-level aggregate is still an open sufficient route, so the
outgoing edge is evidence rather than a logical close.
