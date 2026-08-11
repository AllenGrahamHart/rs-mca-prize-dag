# Dependency sub-DAG

```text
rate_half_ca_hankel_a1_core_free_pole_slack_exclusion [PROVED] --req-->
rate_half_ca_hankel_a1_all_core_sharp_cap_exclusion [PROVED]

rate_half_ca_hankel_a1_fixed_core_pole_slack_exclusion [PROVED] --req--> same
rate_half_ca_hankel_a1_four_contact_low_degree_exclusion [PROVED] --req--> same

rate_half_ca_hankel_a1_all_core_sharp_cap_exclusion
    --ev--> rate_half_band_crossing_location [TARGET]
```
