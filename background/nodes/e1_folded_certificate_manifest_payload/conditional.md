# conditional: e1_folded_certificate_manifest_payload

## Predicate nodes

- `e1_two_cell_folded_manifest_assembly_soundness`
- `e1_folded_certificate_cell_128_payload`
- `e1_folded_certificate_cell_256_payload`

## Claim

Conditional on the two cell transcripts, the E1 folded-certificate manifest
payload holds.

## Proof

The predicate `e1_folded_certificate_cell_128_payload` supplies the complete
named folded certificate for `N'=128`, with zero nonzero non-cyclotomic folded
vectors.

The predicate `e1_folded_certificate_cell_256_payload` supplies the complete
named folded certificate for `N'=256`, with zero nonzero non-cyclotomic folded
vectors.

The proved predicate `e1_two_cell_folded_manifest_assembly_soundness` says
that these two cell records are exactly the complete manifest over
`N' in {128,256}`. Therefore the manifest payload follows from the two cell
payloads.
