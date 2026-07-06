# dependency sub-DAG: ef_ru

Promoted subclaims.

```text
spi_component_control [PROVED]
    -> ef_component_control_alignment [PROVED]

ef_galois_stabilizer_descent [PROVED]
ef_descended_cycle_classification_soundness [PROVED]
ef_pole_free_cycle_exclusion [CONDITIONAL]
    -> ef_full_orbit_pole_forcing [CONDITIONAL]
    -> ef_ru
    -> f1_full_field_pole_forcing

ef_descended_cycle_inventory_payload [TARGET]
    -> ef_descended_cycle_classification_payload [CONDITIONAL]
    -> ef_pole_free_cycle_exclusion [CONDITIONAL]

ef_descended_cycle_classification_payload [CONDITIONAL]
    -> ef_pole_free_cycle_exclusion [CONDITIONAL]

ef_full_orbit_cycle_descent [PROVED]
    -> ef_full_orbit_pole_forcing

ext_import [PROVED]
paid_ext_fn [PROVED]
generating_escape [PROVED]
f1_case_tower [PROVED]
noncontain_degeneracy [PROVED]
    -> EF-POLE / ef_ru context
```

## ef_component_control_alignment

Statement: the extension-fiber alignment incidence has only polynomially many
controlled-degree horizontal components in the relevant row-uniform setup.

Status: PROVED.

## ef_galois_stabilizer_descent

Statement: a horizontal component's Galois stabilizer is full, intermediate,
or trivial/full-orbit; the first two cases are respectively base-descended and
proper-subfield pullback.

Status: PROVED.

## ef_full_orbit_pole_forcing

Statement: a genuinely full-field Galois orbit of horizontal components that
is neither descended nor subfield-confined must lie on the extension-pole
divisor, hence is paid by the existing extension column.

Status: CONDITIONAL. The Galois full-orbit cycle descent and classification
soundness are proved; the active leaf is
`ef_descended_cycle_inventory_payload`.
