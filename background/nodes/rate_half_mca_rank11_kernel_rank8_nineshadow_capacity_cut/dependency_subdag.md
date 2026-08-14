# Dependency sub-DAG

```text
rate_half_mca_rank11_kernel_nine_shadow_containment_capacity_cut
rate_half_mca_rank11_kernel_rank8_nineshadow_extension_deficit
    -> rate_half_mca_rank11_kernel_rank8_nineshadow_capacity_cut
        -> rate_half_band_crossing_location
```

The capacity node strengthens only the proved kernel route interval; it
does not change the status of the downstream target.
