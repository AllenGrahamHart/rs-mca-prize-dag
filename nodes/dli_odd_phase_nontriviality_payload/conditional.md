# conditional: dli_odd_phase_nontriviality_payload

## Predicate nodes

- `dli_odd_phase_polar_obstruction_soundness`
- `dli_odd_phase_polar_obstruction_payload`

## Claim

Conditional on the actual polar-obstruction payload, every DLI odd-evaluation
phase is non-Artin-Schreier on every relevant square-root component.

## Proof

The predicate `dli_odd_phase_polar_obstruction_payload` supplies, for every
central profile, nonzero frequency, DLI harmonic, and relevant square-root
component, an Artin-Schreier-reduced local pole of the phase

```text
P_lambda(sigma(y))
```

whose order is positive and not divisible by `p`.

The proved predicate `dli_odd_phase_polar_obstruction_soundness` says that
such a reduced pole is incompatible with Artin-Schreier triviality
`g^p-g+c`. Therefore each actual DLI odd phase is non-Artin-Schreier, which is
exactly this node's statement.
