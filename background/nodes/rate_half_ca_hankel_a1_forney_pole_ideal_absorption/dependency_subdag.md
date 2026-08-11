# Dependency sub-DAG

```text
rate_half_ca_hankel_exceptional_root_charge [PROVED]
rate_half_ca_hankel_a1_core_stripped_forney_contact_section [PROVED]
                              |
                              +--req-->
rate_half_ca_hankel_a1_forney_pole_ideal_absorption [PROVED]
                              |
                              +--ev--> rate_half_band_crossing_location [TARGET]
```

The node replaces pole interpolation by exact numerator ideal membership.
It creates no conditional.
