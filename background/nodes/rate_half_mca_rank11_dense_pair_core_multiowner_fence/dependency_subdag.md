# Dependency sub-DAG

```text
rate_half_mca_rank11_pair_core_route_cut_import [PROVED]
    |
    | terminal constants and local claim boundary
    v
rate_half_mca_rank11_dense_pair_core_multiowner_fence [PROVED]
    |
    +--> unique/coalesced dense-owner route [REFUTED AS A LOCAL INFERENCE]
    |
    +--> aggregate cross-pair payment or chronology router [OPEN]
```
