# Dependency sub-DAG

```text
rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger [PROVED]
rate_half_ca_hankel_a1_forney_pole_ideal_absorption [PROVED]
rate_half_ca_hankel_a1_direct_three_contact_exclusion [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_first_degree_ambient_defect_factorization [PROVED]
                              |
                              +--ev--> rate_half_band_crossing_location [TARGET]
```

The next leaf applies the exact capacity ledger to bound the residual
domain degree after `B_j` is removed.
