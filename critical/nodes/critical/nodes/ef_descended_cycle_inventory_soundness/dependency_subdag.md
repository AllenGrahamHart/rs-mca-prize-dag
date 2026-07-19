# dependency sub-DAG: ef_descended_cycle_inventory_soundness

Edges are directed from dependency to consumer.

```text
ef_descended_cycle_inventory_soundness [PROVED]
    -> ef_descended_cycle_classification_payload [CONDITIONAL]
```

This proved node checks inventory coverage and allowed labels. It does not
construct the actual EF cycle inventory; that is isolated in
`ef_descended_cycle_inventory_payload`.
