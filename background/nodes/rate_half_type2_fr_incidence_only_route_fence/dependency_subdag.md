# Dependency sub-DAG

```text
rate_half_ca_hankel_endpoint_saturation_rigidity [PROVED]
  --req--> rate_half_type2_fr_incidence_only_route_fence [PROVED]
rate_half_type2_fr_incidence_only_route_fence [PROVED]
  --ev--> rate_half_band_crossing_location [TARGET]
```

The requirement fixes the interpretation of the endpoint incidence axioms.
The outgoing edge is route-selection evidence only.
