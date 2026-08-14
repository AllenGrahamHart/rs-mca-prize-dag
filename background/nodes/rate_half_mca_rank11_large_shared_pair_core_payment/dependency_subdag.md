# Dependency sub-DAG

```text
rate_half_mca_support_local_error_rank_router [PROVED]
                         |
rate_half_mca_rank11_pair_core_route_cut_import [PROVED]
                         |
                         v
rate_half_mca_rank11_large_shared_pair_core_payment [PROVED]
                         |
                         +--> common pair core >= K-4922 [PAID]
                         +--> smaller common core / cross-pair spread [OPEN]
```
