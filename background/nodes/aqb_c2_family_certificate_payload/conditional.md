# conditional: aqb_c2_family_certificate_payload

## Predicate nodes

- `aqb_coupled_family_entropy_manifest_soundness`
- `aqb_coupled_family_entropy_manifest_payload`

## Claim

Conditional on the actual coupled AQB manifest, the `c=2` averaged-family
certificate payload holds.

## Proof

The proved node `aqb_coupled_family_entropy_manifest_soundness` says that a
coupled manifest containing the required family certificate fields and a
ledger keyed to the same family supplies `aqb_c2_family_certificate_payload`.
The remaining predicate `aqb_coupled_family_entropy_manifest_payload` is
exactly the actual manifest. Therefore this payload follows once that
manifest is provided.
