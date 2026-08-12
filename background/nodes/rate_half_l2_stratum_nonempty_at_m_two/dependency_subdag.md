# Dependency sub-DAG

```text
Hankel/polynomial algebra + certificates
                 |
                 v
rate_half_l2_stratum_nonempty_at_m_two [PROVED]
   |
   +-- construction instrument superseded by:
   |   rate_half_l2_stratum_rational_parametrization [PROVED]
   +-- endpoint-profile exclusion (the decisive route) lives at:
   |   rate_half_ca_hankel_endpoint_residual_pole_interpolation_exclusion [PROVED]
   |
   : evidence / kills the emptiness route at m = 2
   v
rate_half_band_crossing_location [TARGET]
```

No requirement edge in. The witness theorem is self-contained by
certificate; the two listed nodes are cross-references (instrument
supersession and the no-contradiction check), not dependencies.
