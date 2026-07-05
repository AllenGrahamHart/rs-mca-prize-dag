# dependency sub-DAG: dli_odd_phase_polar_obstruction_payload

Edges are directed from dependency to consumer.

```text
dli_odd_phase_polar_obstruction_soundness [PROVED]
    -> dli_reduced_phase_manifest_soundness [PROVED]
    -> dli_odd_phase_polar_obstruction_payload [CONDITIONAL]
    -> dli_odd_phase_nontriviality_payload [CONDITIONAL]

dli_reduced_pole_majorant_table_soundness [PROVED]
    -> dli_reduced_phase_manifest_soundness [PROVED]

dli_reduced_phase_manifest_payload [TARGET]
    -> dli_odd_phase_polar_obstruction_payload [CONDITIONAL]
```

This node is now an assembly from reduced-phase manifest soundness plus the
actual DLI reduced-phase manifest.
