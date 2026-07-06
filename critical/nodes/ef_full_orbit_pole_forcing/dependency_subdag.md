# dependency sub-DAG: ef_full_orbit_pole_forcing

```text
ef_galois_stabilizer_descent [PROVED]
    -> ef_full_orbit_cycle_descent [PROVED]
    -> ef_full_orbit_pole_forcing [CONDITIONAL]
    -> ef_ru [CONDITIONAL]

ef_descended_cycle_classification_soundness [PROVED]
    -> ef_pole_free_cycle_exclusion [CONDITIONAL]
    -> ef_full_orbit_pole_forcing [CONDITIONAL]

ef_descended_cycle_inventory_payload [TARGET]
    -> ef_descended_cycle_classification_payload [CONDITIONAL]
    -> ef_pole_free_cycle_exclusion [CONDITIONAL]

ef_descended_cycle_classification_payload [CONDITIONAL]
    -> ef_pole_free_cycle_exclusion [CONDITIONAL]
    -> ef_full_orbit_pole_forcing [CONDITIONAL]
```

The descent of a pole-free full Galois orbit to a `B`-defined cycle is now
closed, and classification soundness is proved. The active EF leaf is the
inventory payload for that descended pole-free cycle.
