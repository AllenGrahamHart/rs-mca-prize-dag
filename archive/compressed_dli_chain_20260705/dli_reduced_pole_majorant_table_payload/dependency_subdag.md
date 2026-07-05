# dependency sub-DAG: dli_reduced_pole_majorant_table_payload

Edges are directed from dependency to consumer.

```text
dli_reduced_pole_majorant_table_soundness [PROVED]
    -> dli_reduced_phase_manifest_soundness [PROVED]
    -> dli_reduced_pole_majorant_table_payload [CONDITIONAL]
    -> dli_reduced_pole_harmonic_ledger [CONDITIONAL]

dli_odd_phase_polar_obstruction_soundness [PROVED]
    -> dli_reduced_phase_manifest_soundness [PROVED]

dli_reduced_phase_manifest_payload [TARGET]
    -> dli_reduced_pole_majorant_table_payload [CONDITIONAL]
```

This node is now an assembly from reduced-phase manifest soundness plus the
actual DLI reduced-phase manifest.
