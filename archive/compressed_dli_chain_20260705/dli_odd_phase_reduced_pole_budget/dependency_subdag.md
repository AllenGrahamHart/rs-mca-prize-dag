# dependency sub-DAG: dli_odd_phase_reduced_pole_budget

```text
dli_artin_schreier_conductor_criterion [PROVED]
    -> dli_odd_phase_noncollapse_conductor [CONDITIONAL]

dli_odd_phase_budget_ledger_soundness [PROVED]
    -> dli_odd_phase_reduced_pole_budget [CONDITIONAL]

dli_odd_phase_polar_obstruction_soundness [PROVED]
    -> dli_odd_phase_nontriviality_payload [CONDITIONAL]

dli_odd_phase_polar_obstruction_payload [TARGET]
    -> dli_odd_phase_nontriviality_payload [CONDITIONAL]

dli_odd_phase_nontriviality_payload [CONDITIONAL]
    -> dli_odd_phase_reduced_pole_budget [CONDITIONAL]

dli_reduced_pole_majorant_table_soundness [PROVED]
    -> dli_reduced_pole_harmonic_ledger [CONDITIONAL]

dli_reduced_pole_majorant_table_payload [TARGET]
    -> dli_reduced_pole_harmonic_ledger [CONDITIONAL]

dli_reduced_pole_harmonic_ledger [CONDITIONAL]
    -> dli_odd_phase_reduced_pole_budget [CONDITIONAL]
    -> dli_odd_phase_noncollapse_conductor [CONDITIONAL]
    -> dli_odd_eval_exponential_sum_bound [CONDITIONAL]
```

The open nodes are `dli_odd_phase_polar_obstruction_payload` and
`dli_reduced_pole_majorant_table_payload`: the project-specific
non-Artin-Schreier certificate payload and reduced-pole accounting payload for
the actual odd-evaluation phase.
