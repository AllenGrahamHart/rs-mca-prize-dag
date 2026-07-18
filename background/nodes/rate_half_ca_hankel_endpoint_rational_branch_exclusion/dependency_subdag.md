# Dependency sub-DAG

```text
rate_half_ca_hankel_endpoint_norm_factorization [PROVED]
  --req--> rate_half_ca_hankel_endpoint_rational_branch_exclusion [PROVED]

rate_half_ca_hankel_endpoint_rational_branch_exclusion [PROVED]
  --ev--> rate_half_band_closure [TARGET]
```

The node classifies every irreducible component bidegree, identifies the
unique dominant defect-one component, and removes the completely
rational-branch stratum.  It does not promote the critical target.
