# Dependency sub-DAG

```text
rate_half_ca_hankel_endpoint_saturation_rigidity [PROVED]
  --req--> rate_half_type2_fr_exact_spend_calibration [PROVED]
  --ev---> rate_half_band_crossing_location [TARGET]
```

The dependency supplies the endpoint tuple and pointwise root-capacity
bound. This node only calibrates the final counting inequality.
