# dependency sub-DAG: dli_reduced_pole_majorant_table_soundness

Edges are directed from dependency to consumer.

```text
dli_reduced_pole_majorant_table_soundness [PROVED]
    -> dli_reduced_pole_harmonic_ledger [CONDITIONAL]
```

This proved node is a formal coverage/domination/summation rule. It does not
construct the actual DLI reduced-pole table; that is isolated in
`dli_reduced_pole_majorant_table_payload`.
