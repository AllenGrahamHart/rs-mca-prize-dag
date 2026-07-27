# Dependency sub-DAG

```text
fm1 [PROVED] -------------------------req-->
                                                 averaged_occupancy_clean_anchor_first_moment_route_cut [PROVED]
averaged_slope_conversion [PROVED] ----req-->

averaged_occupancy_clean_anchor_first_moment_route_cut [PROVED]
    --ev--> unsafe_crossing_family_instantiation [TARGET]
```

The node eliminates one sufficient supplier at the named envelopes. The
evidence edge narrows route ownership and does not discharge the universal
unsafe target.
