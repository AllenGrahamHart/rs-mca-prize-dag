# dependency sub-DAG: xr_profile_minor_certificate_payload

Edges are directed from dependency to consumer.

```text
xr_triangle_eliminant_form [PROVED]
    -> xr_profile_minor_certificate_payload [CONDITIONAL]
    -> xr_profile_minor_certificate_coverage [CONDITIONAL]

xr_triangular_minor_certificate_soundness [PROVED]
    -> xr_profile_minor_record_inventory_soundness [PROVED]

xr_profile_minor_record_inventory_soundness [PROVED]
    -> xr_profile_minor_certificate_payload [CONDITIONAL]

xr_profile_minor_record_inventory_payload [TARGET]
    -> xr_profile_minor_certificate_payload [CONDITIONAL]
    -> xr_profile_minor_certificate_coverage [CONDITIONAL]
```

The open node is now `xr_profile_minor_record_inventory_payload`: the actual
uniform profile-by-profile certificate inventory.
