# Dependency sub-DAG

```text
external_split_design_saturation [PROVED] ---------+
                                                     |
pair_complement_quadratic_trace [PROVED] -----------+--req-->
  dihedral_trace_collision_exclusion [PROVED]
    --ev--> rate_half_band_closure [TARGET]
```

The new node closes the surviving dihedral distance-three external-design
branch. The rate-half band target retains its other proof obligations.
