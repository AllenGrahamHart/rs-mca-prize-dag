# dli_reduced_phase_manifest_payload

- **status:** TARGET
- **closure:** proof or certificate

## Statement

Provide the actual DLI reduced-phase manifest: for every central profile,
nonzero frequency, DLI harmonic, and relevant square-root component, give:

- the Artin-Schreier-reduced local expansion of `P_lambda(sigma(y))`;
- a pole of positive order not divisible by `p`;
- a certified upper bound for the reduced polar divisor of that same phase;
  and
- a proof that the harmonic sum of the majorants is `o(t)`.

## Falsifier

A missing tuple, no prime-to-`p` reduced pole, a majorant below the true
reduced polar divisor, or a harmonic total that is not `o(t)`.
