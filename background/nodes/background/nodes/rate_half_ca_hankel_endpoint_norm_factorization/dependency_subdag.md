# Dependency sub-DAG

```text
rate_half_ca_hankel_endpoint_saturation_rigidity [PROVED]
  --req--> rate_half_ca_hankel_endpoint_norm_factorization [PROVED]

rate_half_ca_hankel_endpoint_norm_factorization [PROVED]
  --ev--> rate_half_band_closure [TARGET]
```

This node proves an algebraic normal form for a hypothetical endpoint failure.
It does not promote the critical target.
