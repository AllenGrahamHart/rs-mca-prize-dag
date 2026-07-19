# Dependency sub-DAG

```text
rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_core_one_middle_adjugate_factorization [PROVED]
                              |
                              +--ev--> rate_half_band_closure [TARGET]
```

This node is an exact coefficient-chain interface for the surviving
core-one high-rank component. It creates no conditional.
