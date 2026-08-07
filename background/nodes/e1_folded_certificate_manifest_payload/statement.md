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

## Round-23 addendum (2026-08-07, coordinator-applied): the N'=256 entry cannot close as written

The round-23 pricing at the six deployed clean-anchor rows (their
declared support bounds): rate-1/4 (2l' = 130) and rate-1/16
(h = 256) are EXPECTED NONEMPTY (class heuristic 2^29-2^39 —
consistent with the banked PRO_W3 ~2^48 full-box figure,
reproduced at 2^48.2); rate-1/8 FLIPS to expected-EMPTY (2^-33 /
2^-39). A manifest demanding "zero nonzero non-cyclotomic folded
vectors in each certificate" therefore cannot close at its
N' = 256 entry even in principle; the manifest needs a per-entry
re-pose (emptiness where expected empty; an explicit
witness-tolerant form where nonempty). Source:
notes/pilots_20260807/ge_lattice_cert/ (price.py, facts.py).
