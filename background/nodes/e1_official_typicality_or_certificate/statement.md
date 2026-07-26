# e1_official_typicality_or_certificate

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For the open E1 cells `N' in {128,256}`, either:

- prove uniform admissible-family typicality for the explicit exceptional
  norm-divisor set; or
- complete folded kernel certificates for named exhibit fields and return no
  nonzero non-cyclotomic folded vector.

This node is reduced to:

- `official_row_primes_pinning`, which fixes the allowed route semantics;
- `e1_folded_certificate_soundness`, which proves the folded no-vector
  certificate route is sound;
- `e1_open_cell_route_soundness`, which proves either route implies this
  predicate; and
- `e1_open_cell_control_payload`, the remaining actual typicality theorem or
  folded-certificate payload.

## Falsifier

An admissible row or named exhibit field with too many non-quotient folded
sparse kernel vectors, a failed/incomplete folded certificate, or a defect in
the route-soundness reduction.
