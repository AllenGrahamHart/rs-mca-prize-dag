# dependency sub-DAG: ef_descended_cycle_classification_payload

Edges are directed from dependency to consumer.

```text
ef_descended_cycle_inventory_soundness [PROVED]
    -> ef_descended_cycle_classification_payload [CONDITIONAL]

ef_descended_cycle_inventory_payload [TARGET]
    -> ef_descended_cycle_classification_payload [CONDITIONAL]
    -> ef_pole_free_cycle_exclusion [CONDITIONAL]
    -> ef_full_orbit_pole_forcing [CONDITIONAL]
    -> ef_ru [CONDITIONAL]
```

The open node is now `ef_descended_cycle_inventory_payload`: the actual EF
pole-free descended-cycle inventory.
