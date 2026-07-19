# dependency sub-DAG: xr_profile_minor_certificate_coverage

```text
xr_triangle_eliminant_form [PROVED]
    -> xr_profile_minor_certificate_payload [CONDITIONAL]
    -> xr_profile_minor_certificate_coverage [CONDITIONAL]
    -> xr_profile_eliminant_nonvanishing [CONDITIONAL]

xr_triangular_minor_certificate_soundness [PROVED]
    -> xr_profile_minor_record_inventory_soundness [PROVED]

xr_profile_minor_record_inventory_soundness [PROVED]
    -> xr_profile_minor_certificate_payload [CONDITIONAL]

xr_profile_minor_record_inventory_payload [TARGET]
    -> xr_profile_minor_certificate_payload [CONDITIONAL]
    -> xr_profile_minor_certificate_coverage [CONDITIONAL]
    -> xr_profile_eliminant_nonvanishing [CONDITIONAL]

xr_triangle_eliminant_form [PROVED]
    -> xr_triangular_minor_certificate_soundness [PROVED]
    -> xr_profile_minor_certificate_coverage [CONDITIONAL]

xr_minor_specialization_certificate_semantics [PROVED]
    -> xr_profile_eliminant_nonvanishing [CONDITIONAL]
```

The open node is `xr_profile_minor_record_inventory_payload`. This node does
not need to reprove that a nonzero specialization certifies nonzero
polynomial identity; that has been factored out as
`xr_minor_specialization_certificate_semantics`.
