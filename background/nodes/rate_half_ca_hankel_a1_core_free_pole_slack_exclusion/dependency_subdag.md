# Dependency sub-DAG

```text
rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger [PROVED]
    --req--> rate_half_ca_hankel_a1_core_free_pole_slack_exclusion [PROVED]

rate_half_ca_hankel_a1_core_free_forney_contact_section [PROVED]
    --req--> same

rate_half_ca_hankel_a1_core_free_pole_slack_exclusion
    --ev--> rate_half_band_crossing_location [TARGET]
```

The two parents respectively supply the exact profile arithmetic and the
contact section used in the vanishing product.
