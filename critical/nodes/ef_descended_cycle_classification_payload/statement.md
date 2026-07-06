# ef_descended_cycle_classification_payload

- **status:** CONDITIONAL
- **closure:** proof

## Statement

Classify every `B`-defined pole-free horizontal cycle in the extension-fiber
incidence, after full-orbit descent, as one of:

- base-descended;
- proper-subfield/tower-confined;
- noncontainment-degenerate.

This is reduced to:

- `ef_descended_cycle_inventory_soundness`, which proves that a complete
  verified inventory implies this classification payload; and
- `ef_descended_cycle_inventory_payload`, which remains to construct the
  actual row-uniform inventory of descended pole-free cycles.

## Falsifier

A `B`-defined pole-free cycle that is not base-descended, not tower-confined,
and survives the noncontainment gate.
