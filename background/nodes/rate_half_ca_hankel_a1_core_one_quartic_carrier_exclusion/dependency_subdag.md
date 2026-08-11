# Dependency sub-DAG

```text
rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger [PROVED]
rate_half_ca_hankel_a1_core_stripped_forney_contact_section [PROVED]
rate_half_ca_hankel_a1_fixed_core_pole_slack_exclusion [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_core_one_quartic_carrier_exclusion [PROVED]
                              |
                              +--ev--> rate_half_band_crossing_location [TARGET]
```

The node closes a larger initial core-one degree prefix. It creates no
conditional dependency.
