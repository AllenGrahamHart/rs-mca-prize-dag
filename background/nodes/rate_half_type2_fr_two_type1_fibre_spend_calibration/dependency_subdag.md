# Dependency sub-DAG

```text
rate_half_ca_hankel_endpoint_saturation_rigidity [PROVED]
  --req--> rate_half_type2_fr_exact_spend_calibration [PROVED]
  --req--> rate_half_type2_fr_two_type1_fibre_spend_calibration [PROVED]
  --ev---> rate_half_band_crossing_location [TARGET]
```

Endpoint saturation supplies the strict pencil setting, support cap, and
outside-incidence ledger. Exact spend calibration supplies the sharp closing
threshold. This node proves what the two-type-1 fibre mechanism actually
pays and isolates its remaining concentration gap.
