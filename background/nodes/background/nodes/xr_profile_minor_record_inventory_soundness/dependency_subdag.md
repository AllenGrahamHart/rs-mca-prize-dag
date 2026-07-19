# dependency sub-DAG: xr_profile_minor_record_inventory_soundness

Edges are directed from dependency to consumer.

```text
xr_triangular_minor_certificate_soundness [PROVED]
    -> xr_profile_minor_record_inventory_soundness [PROVED]
    -> xr_profile_minor_certificate_payload [CONDITIONAL]
```

This proved node checks coverage/dispatch for accepted record types. It does
not construct the actual XR profile inventory; that is isolated in
`xr_profile_minor_record_inventory_payload`.
