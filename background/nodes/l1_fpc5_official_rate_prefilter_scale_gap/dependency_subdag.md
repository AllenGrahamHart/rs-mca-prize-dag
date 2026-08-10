# Dependency sub-DAG

```text
pma_official_rate_small_source_degree_sieve [PROVED] --req--+
                                                            |
l1_fpc5_large_source_exact_prefilter [PROVED] -------req----+
                                                            v
l1_fpc5_official_rate_prefilter_scale_gap [PROVED]
  --ev--> l1_fpc5_large_source_payment [TARGET]
```
