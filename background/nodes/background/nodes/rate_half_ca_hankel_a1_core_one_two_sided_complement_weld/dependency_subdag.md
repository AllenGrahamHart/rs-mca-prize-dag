# Dependency sub-DAG

```text
rate_half_ca_hankel_a1_core_one_component_norm_localization [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_core_one_two_sided_complement_weld [PROVED]
                              |
                              +--ev--> rate_half_band_closure [TARGET]
```

The node turns the two exact complement directions into one matrix
factorization constraint. It creates no conditional.
