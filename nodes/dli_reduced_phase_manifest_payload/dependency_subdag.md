# dependency sub-DAG: dli_reduced_phase_manifest_payload

Edges are directed from dependency to consumer.

```text
dli_reduced_phase_manifest_payload [TARGET]
    -> dli_odd_phase_polar_obstruction_payload [CONDITIONAL]
    -> dli_odd_phase_nontriviality_payload [CONDITIONAL]

dli_reduced_phase_manifest_payload [TARGET]
    -> dli_reduced_pole_majorant_table_payload [CONDITIONAL]
    -> dli_reduced_pole_harmonic_ledger [CONDITIONAL]
```

This target supplies both DLI reduced local pole witnesses and the reduced
polar-divisor majorant table.
