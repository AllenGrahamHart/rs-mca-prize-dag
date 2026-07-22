# Dependency sub-DAG

```text
ww_paid_residual_partition_adapter [PROVED] --req-->
  ww_two_class_minimal_ledger_reduction [PROVED]
    --ev--> ww_row_envelope_clause [TARGET, RETIRED]

ww_lemma_a_exhaustion [PROVED] --ev--> two-class reduction
```

The partition dependency supplies the exact additive identity. Lemma A gives
useful residual structure but is not required for the identity. The identity
survives and is used by the exact unsafe-cell scope counterexample.
