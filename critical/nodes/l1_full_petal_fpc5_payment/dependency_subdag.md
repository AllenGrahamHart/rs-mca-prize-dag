# Dependency sub-DAG

```text
petal_growth [PROVED top band] --------------------------+
pma_petal_pattern_root_pinning_ledger [PROVED E=0] -----+--> pma_full_petal_band_composition [PROVED]
e22_two_class_exhaustion [PROVED] -----------------------+

pma_full_petal_band_composition [PROVED] --ev-->
  l1_full_petal_fpc5_payment [CONDITIONAL] --req--> imgfib [CONDITIONAL]

l1_fpc5_ratehalf_m4_t3_split_slice_payment [TARGET] --req--+
l1_fpc5_m4_t2_payment [CONDITIONAL] ----------------req--+--> l1_full_petal_fpc5_payment
l1_fpc5_large_source_payment [TARGET] ---------------req--+
```

The strict proved reduction suppliers are also req-wired in `node.json`.
