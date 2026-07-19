# conditional: ef_pole_free_cycle_exclusion

This node is conditional on:

- `ef_full_orbit_cycle_descent`
- `ef_descended_cycle_classification_soundness`
- `ef_descended_cycle_classification_payload`

The first two dependencies are proved. The classification payload is now
conditional on the live inventory payload, which must classify every descended
`B`-defined pole-free horizontal cycle as base-descended,
proper-subfield/tower-confined, or noncontainment-degenerate.
