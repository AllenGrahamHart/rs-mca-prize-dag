# e1_open_cell_control_payload

- **status:** see dag.json (single source of truth; dag status PROVED) [header retrofit 2026-07-10, catch #69 — was: CONDITIONAL]
- **closure:** proof

## Statement

For the open E1 cells `N' in {128,256}`, provide one of:

- a uniform admissible-family typicality theorem for the explicit
  norm-divisor exceptional set; or
- named exhibit fields together with complete folded kernel certificates
  returning no nonzero non-cyclotomic folded vector.

The payload must declare which route it takes, in the sense of
`official_row_primes_pinning`.

This node is reduced through the named folded-certificate route to:

- `e1_folded_certificate_manifest_soundness`, which proves that a complete
  manifest for `N' in {128,256}` implies this payload; and
- `e1_folded_certificate_manifest_payload`, now conditional on the actual
  `N'=128` and `N'=256` cell certificate payloads.

## Falsifier

Missing coverage for `N'=128` or `N'=256`, a failed or incomplete folded
certificate, or an admissible-family row whose exceptional incidence exceeds
the allowed budget.
