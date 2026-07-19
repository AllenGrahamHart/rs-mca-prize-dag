# Dependency sub-DAG

```text
rate_half_ca_hankel_a1_core_one_max_component_localization [PROVED] --req--+
                                                                         |
rate_half_ca_hankel_a1_core_one_middle_adjugate_factorization [PROVED] ---+
                                                                         v
rate_half_ca_hankel_a1_core_one_component_norm_localization [PROVED]
                                                                         |
                                                                         +--ev--> rate_half_band_closure [TARGET]
```

The node localizes the exact remaining mixed norm object and creates no
conditional.
