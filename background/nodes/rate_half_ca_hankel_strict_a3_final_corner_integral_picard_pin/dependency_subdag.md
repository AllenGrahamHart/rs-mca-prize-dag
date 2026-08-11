# Dependency sub-DAG

```text
rate_half_ca_hankel_strict_a3_slope_slack_contact_exclusion [PROVED]
    --req-->
rate_half_ca_hankel_strict_a3_final_corner_integral_picard_pin [PROVED]
    --ev--> rate_half_band_crossing_location [TARGET]

rate_half_ca_hankel_endpoint_forney_infinity_contact_section [PROVED]
    --req--> same
```

The slope node supplies the exact corner and pole budget. The contact node
supplies the degree-one section. Univariate descent makes that section
componentwise nonzero and collapses the component arithmetic.
