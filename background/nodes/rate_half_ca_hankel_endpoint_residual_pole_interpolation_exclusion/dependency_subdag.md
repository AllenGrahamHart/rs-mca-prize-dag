# Dependency sub-DAG

```text
rate_half_ca_hankel_endpoint_component_defect_localization [PROVED]
    --req-->
rate_half_ca_hankel_endpoint_residual_pole_interpolation_exclusion [PROVED]
    --ev--> rate_half_band_crossing_location [TARGET]

rate_half_ca_hankel_endpoint_forney_infinity_contact_section [PROVED]
    --req--> same
```

The component parent bounds the pole colength and makes low-domain-degree
interpolation componentwise nonzero. The contact parent provides the
fourfold section whose official arithmetic cancels all `m`-scale terms.
