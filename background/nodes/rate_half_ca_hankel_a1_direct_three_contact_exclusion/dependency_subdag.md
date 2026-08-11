# Dependency sub-DAG

```text
rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger [PROVED]
rate_half_ca_hankel_a1_forney_pole_ideal_absorption [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_direct_three_contact_exclusion [PROVED]
                              |
                              +--ev--> rate_half_band_crossing_location [TARGET]
```

This closes larger initial prefixes in both live core branches and retires
the earlier first core-one cubic corner as a live endpoint.
