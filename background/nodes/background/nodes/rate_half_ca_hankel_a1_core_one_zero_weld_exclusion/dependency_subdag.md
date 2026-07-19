# Dependency sub-DAG

```text
rate_half_ca_hankel_a1_core_one_zero_weld_quartic_boundary [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_core_one_zero_weld_exclusion [PROVED]
                              |
                              +--ev--> rate_half_band_closure [TARGET]
```

The node closes the `K=0` branch without introducing a conditional. The
`K!=0` weld remains an explicit open branch of the critical consumer.
