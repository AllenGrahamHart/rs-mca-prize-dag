# dependency sub-DAG: dli_odd_phase_nontriviality_payload

Edges are directed from dependency to consumer.

```text
dli_artin_schreier_conductor_criterion [PROVED]
    -> dli_odd_phase_polar_obstruction_soundness [PROVED]

dli_odd_phase_polar_obstruction_soundness [PROVED]
    -> dli_odd_phase_nontriviality_payload [CONDITIONAL]

dli_odd_phase_polar_obstruction_payload [TARGET]
    -> dli_odd_phase_nontriviality_payload [CONDITIONAL]
    -> dli_odd_phase_reduced_pole_budget [CONDITIONAL]
```

The open node is now `dli_odd_phase_polar_obstruction_payload`: the actual
local expansion/cancellation certificate for the DLI odd phases.
