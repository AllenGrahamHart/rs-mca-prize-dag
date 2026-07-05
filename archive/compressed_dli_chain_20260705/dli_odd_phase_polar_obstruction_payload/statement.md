# dli_odd_phase_polar_obstruction_payload

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For every central profile, nonzero frequency, DLI harmonic, and relevant
square-root component, construct a local certificate showing that the
Artin-Schreier-reduced odd-evaluation phase

```text
P_lambda(sigma(y))
```

has a pole of positive order not divisible by `p`.

This is reduced to:

- `dli_reduced_phase_manifest_soundness`, the proved rule that a reduced
  phase manifest supplies the local polar-obstruction payload; and
- `dli_reduced_phase_manifest_payload`, the remaining actual DLI reduced
  phase manifest.

## Falsifier

An actual DLI odd phase whose Artin-Schreier-reduced local expansions have no
positive pole order prime to `p`.
