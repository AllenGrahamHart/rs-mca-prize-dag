# ATTACK - e1_folded_certificate_manifest_payload

This is now an E1 assembly node. The cell nodes are conditional on the proved
field/soundness split, so the live leaves are:

- `e1_folded_no_vector_certificate_128_payload`;
- `e1_folded_no_vector_certificate_256_payload`.

Needed output:

- provide the complete folded kernel certificate transcript for each cell;
- verify that each transcript is complete and returns zero nonzero
  non-cyclotomic folded vectors; and
- keep the manifest tied to named fields, not to a nonexistent hidden list of
  official row primes.

The common exhibit field and primitive roots are now proved by
`e1_pocklington_250bit_exhibit_field`. The toy `N'=16` folded replay is only a
soundness check. It does not close either no-vector payload.
