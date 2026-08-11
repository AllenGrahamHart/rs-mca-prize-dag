# Dependency sub-DAG

```text
rate_half_ca_hankel_endpoint_rational_normal_kernel_curve [PROVED]
    --req-->
rate_half_ca_hankel_endpoint_forney_infinity_contact_section [PROVED]
    --req-->
rate_half_ca_hankel_endpoint_residual_pole_interpolation_exclusion [PROVED]

rate_half_ca_hankel_endpoint_component_defect_localization [PROVED]
    --req--> both nodes
```

The kernel parent supplies the exact degree and all recurrence rows. The
component parent supplies reducedness and rules out horizontal or vertical
components, allowing the local contact quotient to be used globally.
