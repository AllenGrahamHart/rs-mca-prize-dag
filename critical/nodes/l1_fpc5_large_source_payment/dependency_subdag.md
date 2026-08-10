# Dependency sub-DAG

```text
pma_official_rate_small_source_degree_sieve [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_large_source_exact_prefilter [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_tpetal_saturated_slice_dimension [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_tpetal_anchor_coordinate [PROVED] --ev-->
  l1_fpc5_large_source_payment [TARGET]
l1_fpc5_large_source_payment [TARGET]
  --req--> l1_full_petal_fpc5_payment [CONDITIONAL]
```
