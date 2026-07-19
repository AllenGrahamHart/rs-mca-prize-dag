# Dependency sub-DAG

```text
rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_core_one_max_component_localization [PROVED]
                              |
                              +--ev--> rate_half_band_closure [TARGET]
```

This node removes all separation-rank-at-most-four dominant models from one
sharp-cap face. It creates no conditional and does not close that face.
