# Dependency sub-DAG

```text
f3_h3_rich_fiber_norm_cutoff [PROVED] ------------------------req--+
f3_h3_rich_fiber_ideal_batching [PROVED] ---------------------req--+--> f3_h3_weighted_multistar_router [PROVED]
f3_h3_distance_two_collision_2primary_exclusion [PROVED] -----req--+                    |
                                                                                         ev
                                                                                          |
                                                                                          v
                                                              f3_h3_mobius_excess_half [TARGET]
```
