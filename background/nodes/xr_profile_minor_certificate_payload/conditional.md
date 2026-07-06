# conditional: xr_profile_minor_certificate_payload

## Predicate nodes

- `xr_profile_minor_record_inventory_soundness`
- `xr_profile_minor_record_inventory_payload`

## Claim

Conditional on the actual XR profile record inventory, every budget-meeting
unpaid non-boundary light profile has an accepted nonzero maximal-minor
certificate payload record.

## Proof

The predicate `xr_profile_minor_record_inventory_payload` supplies an
inventory covering every required light-triangle profile. For each profile it
assigns one record of an accepted type: triangular with nonzero diagonal,
monomial/noncancellation-certified, or a complete remote nonzero-minor table
record.

The proved predicate `xr_profile_minor_record_inventory_soundness` says that
such a complete inventory implies exactly the payload statement. Therefore
`xr_profile_minor_certificate_payload` holds under the actual inventory
payload.
