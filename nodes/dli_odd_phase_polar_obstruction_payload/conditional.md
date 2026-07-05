# conditional: dli_odd_phase_polar_obstruction_payload

## Predicate nodes

- `dli_reduced_phase_manifest_soundness`
- `dli_reduced_phase_manifest_payload`

## Claim

Conditional on the actual DLI reduced-phase manifest, the odd-phase polar
obstruction payload holds.

## Proof

The proved node `dli_reduced_phase_manifest_soundness` says that a manifest
covering every DLI tuple with an Artin-Schreier-reduced local expansion and a
positive pole order not divisible by `p` supplies this payload. The remaining
predicate `dli_reduced_phase_manifest_payload` is exactly the actual manifest.
Therefore the payload follows once that manifest is provided.
