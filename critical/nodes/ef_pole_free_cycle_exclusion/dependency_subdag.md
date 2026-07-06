# dependency sub-DAG: ef_pole_free_cycle_exclusion

```text
ef_galois_stabilizer_descent [PROVED]
    -> ef_full_orbit_cycle_descent [PROVED]
    -> ef_full_orbit_pole_forcing [CONDITIONAL]

ef_descended_cycle_classification_soundness [PROVED]
    -> ef_pole_free_cycle_exclusion [CONDITIONAL]
    -> ef_full_orbit_pole_forcing [CONDITIONAL]
    -> ef_ru [CONDITIONAL]

ef_descended_cycle_inventory_soundness [PROVED]
    -> ef_descended_cycle_classification_payload [CONDITIONAL]

ef_descended_cycle_inventory_payload [TARGET]
    -> ef_descended_cycle_classification_payload [CONDITIONAL]
    -> ef_pole_free_cycle_exclusion [CONDITIONAL]

ef_descended_cycle_classification_payload [CONDITIONAL]
    -> ef_pole_free_cycle_exclusion [CONDITIONAL]
    -> ef_full_orbit_pole_forcing [CONDITIONAL]
    -> ef_ru [CONDITIONAL]
```

The open target is now the descended-cycle inventory payload.
Pricing of actual pole intersections remains handled by the existing
extension-pole ledger.
