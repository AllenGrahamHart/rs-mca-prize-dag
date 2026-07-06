# dependency sub-DAG: xr_profile_eliminant_nonvanishing

```text
xr_triangle_eliminant_form [PROVED]
    -> xr_minor_specialization_certificate_semantics [PROVED]
    -> xr_profile_eliminant_nonvanishing [CONDITIONAL]
    -> xr_eliminant_vanishing_class [CONDITIONAL]

xr_triangle_eliminant_form [PROVED]
    -> xr_profile_minor_certificate_payload [CONDITIONAL]
    -> xr_profile_minor_certificate_coverage [CONDITIONAL]
    -> xr_profile_eliminant_nonvanishing [CONDITIONAL]

xr_profile_minor_record_inventory_payload [TARGET]
    -> xr_profile_minor_certificate_payload [CONDITIONAL]
    -> xr_profile_minor_certificate_coverage [CONDITIONAL]
    -> xr_profile_eliminant_nonvanishing [CONDITIONAL]

xr_triangle_eliminant_form [PROVED]
    -> xr_triangular_minor_certificate_soundness [PROVED]
    -> xr_profile_minor_certificate_coverage [CONDITIONAL]
```

## Closed component

`xr_minor_specialization_certificate_semantics` proves that one admissible
specialization with nonzero determinant certifies a nonzero maximal-minor
polynomial on the profile chart.

## Open component

`xr_profile_minor_record_inventory_payload` must produce such a certificate
record for every budget-meeting unpaid non-boundary light profile.
