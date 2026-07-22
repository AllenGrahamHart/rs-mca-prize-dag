# Dependency sub-DAG

```text
quadratic_locator_rank_gate [PROVED] --------+
                                               +--req--> saturated_cyclic_design_residue_route_fence [PROVED]
complement_residue_rank_three_gate [PROVED] --+                                  |
                                                                                  +--ev--> rate_half_band_closure [UNPROVED]
```

The construction kills the conjunction of the two uncalibrated rank shadows,
while confirming that the actual rank-three residue condition separates the
cyclic survivor.
