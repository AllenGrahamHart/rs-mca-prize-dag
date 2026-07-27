# conditional: e1_open_cell_control_payload

## Predicate nodes

- `e1_folded_certificate_manifest_soundness`
- `e1_folded_certificate_manifest_payload`

## Claim

Conditional on the actual folded-certificate manifest, the E1 open-cell
control payload holds through the named folded-certificate route.

## Proof

The predicate `e1_folded_certificate_manifest_payload` supplies named exhibit
fields for both open cells `N'=128` and `N'=256`, together with complete
folded kernel certificate records returning no nonzero non-cyclotomic folded
vector. That manifest predicate is now assembled from the two explicit cell
payloads.

The proved predicate `e1_folded_certificate_manifest_soundness` says that a
manifest with exactly those fields satisfies the named folded-certificate
route of `e1_open_cell_control_payload`. Therefore this node follows.
