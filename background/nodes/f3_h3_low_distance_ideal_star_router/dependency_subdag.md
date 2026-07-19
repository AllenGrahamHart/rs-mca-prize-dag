# Dependency sub-DAG

```text
f3_h3_rich_fiber_norm_cutoff [PROVED] --------req-->
                                                   \
                                                    f3_h3_low_distance_ideal_star_router [PROVED]
                                                   /                                      |
f3_h3_rich_fiber_ideal_batching [PROVED] -----req-->                                       ev
                                                   \                                      |
f3_h3_distance_two_collision_2primary_exclusion [PROVED] --req-->                         |
                                                                                           |
                                                                                           v
                                                               f3_h3_mobius_excess_half [TARGET]
```

The new node is theorem-level evidence. It replaces the single collision norm
by a normalized two-generator ideal but does not make the critical leaf
conditional or proved.
