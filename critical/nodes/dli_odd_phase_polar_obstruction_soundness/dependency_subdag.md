# dependency sub-DAG: dli_odd_phase_polar_obstruction_soundness

Edges are directed from dependency to consumer.

```text
dli_artin_schreier_conductor_criterion [PROVED]
    -> dli_odd_phase_polar_obstruction_soundness [PROVED]
    -> dli_odd_phase_nontriviality_payload [CONDITIONAL]
```

This proved node is a formal certificate-soundness rule. It does not construct
the DLI local expansions; those are isolated in
`dli_odd_phase_polar_obstruction_payload`.
