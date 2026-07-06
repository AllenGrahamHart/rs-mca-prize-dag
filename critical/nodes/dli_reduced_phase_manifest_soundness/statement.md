# dli_reduced_phase_manifest_soundness

- **status:** PROVED
- **closure:** proof

## Statement

Suppose a reduced-phase manifest covers every central profile, nonzero
frequency, DLI harmonic, and relevant square-root component, and for each
tuple supplies:

- the Artin-Schreier-reduced local expansion of `P_lambda(sigma(y))`;
- a pole of positive order not divisible by `p`;
- a certified upper bound for the reduced polar divisor of the same phase;
  and
- a proof that the harmonic sum of the majorants is `o(t)`.

Then both payloads hold:

- `dli_odd_phase_polar_obstruction_payload`;
- `dli_reduced_pole_majorant_table_payload`.

## Falsifier

A verified reduced-phase manifest satisfying the pole and majorant predicates
while one of the two DLI payloads fails.
