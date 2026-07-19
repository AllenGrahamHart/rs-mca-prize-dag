# ef_pole_free_cycle_exclusion

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: CONDITIONAL]
- **closure:** proof

## Statement

No `B`-defined horizontal cycle in the extension-fiber pole complement, after
removing base-descended components, proper-subfield pullbacks, and
noncontainment-degenerate residues, can survive as an unpaid full-field
hidden-fiber leakage class.

Combined with `ef_full_orbit_cycle_descent`, this excludes full Galois orbits
of horizontal components avoiding the extension-pole divisor.

This node is reduced to:

- `ef_descended_cycle_classification_soundness`, the proved rule that an
  exhaustive base/tower/noncontainment classification excludes hidden
  pole-free leakage; and
- `ef_descended_cycle_classification_payload`, which reduces row-uniform
  classification to the actual descended-cycle inventory payload.

## Falsifier

A `B`-defined pole-free horizontal cycle in the extension-fiber incidence that
is not base-descended, not tower-confined, survives noncontainment, or exposes
a defect in the classification-soundness rule.
