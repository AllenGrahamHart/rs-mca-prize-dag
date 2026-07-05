# dli_reduced_pole_majorant_table_payload

- **status:** CONDITIONAL
- **closure:** proof

## Statement

Construct the actual DLI reduced-pole majorant table: for every central
profile, nonzero frequency, DLI harmonic, and relevant square-root component,
bound the Artin-Schreier-reduced polar divisor of

```text
P_lambda(sigma(y))
```

and prove that the harmonic sum of the table is `o(t)`.

This is reduced to:

- `dli_reduced_phase_manifest_soundness`, the proved rule that a reduced
  phase manifest supplies the majorant table payload; and
- `dli_reduced_phase_manifest_payload`, the remaining actual DLI reduced
  phase manifest.

## Falsifier

An actual DLI tuple whose reduced polar divisor exceeds the table entry, or a
table whose harmonic total is not `o(t)`.
