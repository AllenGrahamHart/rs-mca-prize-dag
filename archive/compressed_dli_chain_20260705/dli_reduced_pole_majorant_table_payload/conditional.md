# conditional: dli_reduced_pole_majorant_table_payload

## Predicate nodes

- `dli_reduced_phase_manifest_soundness`
- `dli_reduced_phase_manifest_payload`

## Claim

Conditional on the actual DLI reduced-phase manifest, the reduced-pole
majorant table payload holds.

## Proof

The proved node `dli_reduced_phase_manifest_soundness` says that a manifest
covering every DLI tuple with certified polar-divisor majorants and an `o(t)`
harmonic total supplies this payload. The remaining predicate
`dli_reduced_phase_manifest_payload` is exactly the actual manifest.
Therefore the payload follows once that manifest is provided.
