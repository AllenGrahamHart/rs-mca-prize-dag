# Dependency sub-DAG

```text
rate_half_mca_rank11_relative_correction_tenflat_collapse [PROVED]
rate_half_mca_rank11_global_core_rankdrop_highcomplexity_router [PROVED]
                                  |
                                  v
rate_half_mca_rank11_relative_rankflat_kernel_shortening_router [PROVED]
                         /                         \
                vertical: one slope       kernel rank <=9: paid
                                  |
                                  v
                   component aggregation / chronology [OPEN]
```

All individual rank-flat components are routed; only their aggregate remains.
