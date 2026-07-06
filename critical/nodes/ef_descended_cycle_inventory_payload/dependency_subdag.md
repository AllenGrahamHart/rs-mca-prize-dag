# dependency sub-DAG: ef_descended_cycle_inventory_payload

Edges are directed from dependency to consumer.

```text
ef_descended_cycle_inventory_payload [TARGET]
    -> ef_descended_cycle_classification_payload [CONDITIONAL]
    -> ef_pole_free_cycle_exclusion [CONDITIONAL]
```

This target is the project-specific EF pole-free descended-cycle inventory.
