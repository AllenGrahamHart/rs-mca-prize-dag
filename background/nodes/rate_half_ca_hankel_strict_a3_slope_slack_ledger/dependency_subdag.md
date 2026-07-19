# Dependency sub-DAG

```text
rate_half_ca_hankel_minimal_index_budget [PROVED] --------req---+
                                                               |
rate_half_ca_hankel_exceptional_root_charge [PROVED] ----req---+
                                                               v
rate_half_ca_hankel_strict_a3_slope_slack_ledger [PROVED]
                                                               |
                                                               +--ev--> rate_half_band_closure [TARGET]
```

The theorem creates no conditional node. It generalizes the former
`e=m,h=0` endpoint geometry to every live strict `A=3` parameter degree and
leaves the printed `(e,h)` strata as direct open cases of the existing
critical target.
