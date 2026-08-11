# Dependency sub-DAG

```text
rate_half_ca_hankel_strict_a3_slope_slack_ledger [PROVED]
    --req-->
rate_half_ca_hankel_strict_a3_slope_slack_contact_exclusion [PROVED]
    --ev--> rate_half_band_crossing_location [TARGET]

rate_half_ca_hankel_endpoint_forney_infinity_contact_section [PROVED]
    --req--> same
```

The first parent supplies the exact `(e,delta,h,O)` ledger. The second turns
the Hankel recurrence into a section of degree `delta`; pole interpolation
then spends at most the same `delta` conditions.
