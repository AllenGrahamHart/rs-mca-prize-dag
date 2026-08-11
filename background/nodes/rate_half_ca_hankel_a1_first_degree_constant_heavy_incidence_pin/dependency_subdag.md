# Dependency sub-DAG

```text
rate_half_ca_hankel_a1_forney_pole_ideal_absorption [PROVED]
rate_half_ca_hankel_a1_first_degree_ambient_defect_factorization [PROVED]
rate_half_ca_hankel_a1_first_degree_bounded_residual_table [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_first_degree_constant_heavy_incidence_pin [PROVED]
                              |
                              +--ev--> rate_half_band_crossing_location [TARGET]
```

The smallest remaining constant residuals have only one or two total gaps
from simultaneous omission and excess-incidence saturation.
