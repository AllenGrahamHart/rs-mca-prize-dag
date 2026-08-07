# Dependency sub-DAG

```text
petal_growth [PROVED top band] --------------------------+
pma_petal_pattern_root_pinning_ledger [PROVED E=0] -----+--> pma_full_petal_band_composition [PROVED]
e22_two_class_exhaustion [PROVED] -----------------------+

pma_full_petal_band_composition [PROVED] --ev-->
  l1_full_petal_fpc5_payment [TARGET] --req--> imgfib [CONDITIONAL]
```

The proved composition identifies FPC5 exactly but does not count it. The
TARGET is intentionally a red leaf.
