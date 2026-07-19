# Dependency sub-DAG

```text
rate_half_ca_hankel_minimal_index_budget [PROVED] --------req---+
                                                               |
rate_half_ca_hankel_exceptional_root_charge [PROVED] ----req---+
                                                               v
rate_half_ca_hankel_half_distance_a3_slope_slack_ledger [PROVED]
                                                               |
                                                               +--ev--> rate_half_band_closure [TARGET]
```

This is the transpose-shaped half-distance `A=3` branch. It creates no
conditional and makes no inference about the separate `A=1` rows.
