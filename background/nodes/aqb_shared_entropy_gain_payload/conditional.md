# conditional: aqb_shared_entropy_gain_payload

## Predicate nodes

- `aqb_coupled_family_entropy_manifest_soundness`
- `aqb_coupled_family_entropy_manifest_payload`

## Claim

Conditional on the actual coupled AQB manifest, the entropy-gain payload
holds for the averaged `c=2` family.

## Proof

The proved node `aqb_coupled_family_entropy_manifest_soundness` says that a
coupled manifest containing exact or interval-certified ledger entries keyed
to the same family certificate supplies `aqb_shared_entropy_gain_payload`.
The remaining predicate `aqb_coupled_family_entropy_manifest_payload` is the
actual manifest. Therefore this payload follows once that manifest is
provided.
