# dependency sub-DAG: dli_reduced_pole_harmonic_ledger

Edges are directed from dependency to consumer.

```text
dli_reduced_pole_majorant_table_soundness [PROVED]
    -> dli_reduced_pole_harmonic_ledger [CONDITIONAL]

dli_reduced_pole_majorant_table_payload [TARGET]
    -> dli_reduced_pole_harmonic_ledger [CONDITIONAL]
    -> dli_odd_phase_reduced_pole_budget [CONDITIONAL]
```

The open node is now `dli_reduced_pole_majorant_table_payload`: the actual
DLI reduced-pole table and its harmonic summation.
