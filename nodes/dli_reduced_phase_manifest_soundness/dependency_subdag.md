# dependency sub-DAG: dli_reduced_phase_manifest_soundness

Edges are directed from dependency to consumer.

```text
dli_odd_phase_polar_obstruction_soundness [PROVED]
    -> dli_reduced_phase_manifest_soundness [PROVED]
    -> dli_odd_phase_polar_obstruction_payload [CONDITIONAL]
    -> dli_odd_phase_nontriviality_payload [CONDITIONAL]

dli_reduced_pole_majorant_table_soundness [PROVED]
    -> dli_reduced_phase_manifest_soundness [PROVED]
    -> dli_reduced_pole_majorant_table_payload [CONDITIONAL]
    -> dli_reduced_pole_harmonic_ledger [CONDITIONAL]

dli_reduced_phase_manifest_payload [TARGET]
    -> dli_odd_phase_polar_obstruction_payload [CONDITIONAL]

dli_reduced_phase_manifest_payload [TARGET]
    -> dli_reduced_pole_majorant_table_payload [CONDITIONAL]
```

This node proves only reduced-phase manifest semantics. The actual local
expansions and majorant table are supplied by the payload node.
