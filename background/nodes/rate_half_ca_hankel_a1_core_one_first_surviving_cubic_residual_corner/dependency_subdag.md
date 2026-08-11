# Dependency sub-DAG

```text
rate_half_ca_hankel_a1_core_one_quartic_carrier_exclusion [PROVED]
rate_half_ca_hankel_a1_core_one_general_middle_adjugate_factorization [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_core_one_first_surviving_cubic_residual_corner [PROVED]
                              |
                              +--ev--> rate_half_band_crossing_location [TARGET]
```

The corner node exposes a degree-at-most-three residual factor as the next
finite-defect object. It creates no conditional.
