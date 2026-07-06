# dependency sub-DAG: ef_descended_cycle_classification_soundness

Edges are directed from dependency to consumer.

```text
ef_full_orbit_cycle_descent [PROVED]
    -> ef_descended_cycle_classification_soundness [PROVED]
    -> ef_pole_free_cycle_exclusion [CONDITIONAL]

ef_component_control_alignment [PROVED]
    -> ef_descended_cycle_classification_soundness [PROVED]

ef_galois_stabilizer_descent [PROVED]
    -> ef_descended_cycle_classification_soundness [PROVED]
```

This node proves only that an exhaustive base/tower/noncontainment
classification eliminates the hidden pole-free leakage class. It does not
provide the classification.
