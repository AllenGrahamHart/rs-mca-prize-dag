# e1_folded_certificate_manifest_payload

- **status:** CONDITIONAL
- **closure:** proof or certificate

## Statement

Construct the actual named folded-certificate manifest for the E1 open cells
`N' in {128,256}`, with:

- a named exhibit field for each cell;
- a complete folded kernel certificate record for each cell; and
- zero nonzero non-cyclotomic folded vectors in each certificate.

This node is reduced to:

- `e1_two_cell_folded_manifest_assembly_soundness`, which proves that the two
  cell transcripts assemble to the manifest; and
- the two remaining cell payloads:
  `e1_folded_certificate_cell_128_payload` and
  `e1_folded_certificate_cell_256_payload`.

## Falsifier

Missing `N'=128` or `N'=256` manifest entry, an incomplete folded
certificate, or a nonzero folded vector in a listed certificate.
