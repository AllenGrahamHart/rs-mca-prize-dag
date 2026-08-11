# Dependency sub-DAG

```text
rate_half_ca_hankel_strict_a3_final_corner_integral_picard_pin [PROVED]
    --req-->
rate_half_ca_hankel_strict_a3_final_corner_divisor_exclusion [PROVED]
    --ev--> rate_half_band_crossing_location [TARGET]

rate_half_ca_hankel_strict_a3_slope_slack_contact_exclusion [PROVED]
    --req--> same
```

The Picard parent supplies the univariate complete-fibre divisor identity.
The slope parent proves this is the only strict profile requiring exclusion.
