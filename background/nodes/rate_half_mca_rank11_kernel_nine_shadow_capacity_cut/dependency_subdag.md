# Dependency sub-DAG

```text
rate_half_mca_rank11_kernel_hybrid_capacity_cut [PROVED]
  + rate_half_mca_rank11_kernel_nine_shadow_coupling [PROVED]
  -> rate_half_mca_rank11_kernel_nine_shadow_capacity_cut [PROVED]
  -> rate_half_band_crossing_location [CONJECTURE, evidence only]
```

This cut changes the exact kernel interval boundary but does not close the
downstream rate-half target.
