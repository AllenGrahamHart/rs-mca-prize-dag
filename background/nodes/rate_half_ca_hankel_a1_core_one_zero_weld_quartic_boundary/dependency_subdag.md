# Dependency sub-DAG

```text
rate_half_ca_hankel_a1_core_one_two_sided_complement_weld [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_core_one_zero_weld_quartic_boundary [PROVED]
                              |
                              +--ev--> rate_half_band_closure [TARGET]
```

The node excludes every zero-weld profile except one exact quartic separated
boundary. It creates no conditional.
