# dli_odd_phase_nontriviality_payload

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For every central profile, nonzero frequency, DLI harmonic, and relevant
square-root component, prove the actual odd-evaluation phase

```text
P_lambda(sigma(y))
```

is not of Artin-Schreier form

```text
g^p - g + c.
```

This is reduced to:

- `dli_odd_phase_polar_obstruction_soundness`, which proves that a verified
  reduced pole of order prime to `p` rules out Artin-Schreier triviality; and
- `dli_odd_phase_polar_obstruction_payload`, which remains to construct those
  reduced local pole certificates for the actual DLI odd phases.

## Falsifier

An actual DLI component and nonzero frequency for which
`P_lambda(sigma(y)) = g^p-g+c`.
