# Dependency sub-DAG

```text
rate_half_ca_hankel_clean_endpoint_forney_resultant_regular_factor [PROVED]
    --req-->
rate_half_ca_hankel_clean_endpoint_picard_forney_contact_exclusion [PROVED]
    --ev--> rate_half_band_crossing_location [TARGET]

rate_half_ca_hankel_clean_endpoint_two_axis_resultant_picard_pin [PROVED]
    --req--> same
```

The first parent supplies the canonical numerator, all `rho+2` recurrence
rows, its bidegree, and nonvanishing on `C`. The second supplies the effective
degree-one class `O_C(N,-T)=O_C(P_*)`. Their tensor combination lands in a
surface line bundle with a direct vanishing calculation.
