# Dependency sub-DAG

```text
rate_half_ca_hankel_minimal_index_budget [PROVED] --------req---+
                                                               |
rate_half_ca_hankel_exceptional_root_charge [PROVED] ----req---+
                                                               v
rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger [PROVED]
                                                               |
                                                               +--ev--> rate_half_band_closure [TARGET]
```

The node strips the already-proved fixed core before forming its residual
incidence matrix. It creates no conditional and excludes no residual stratum.
