# frontier: e1_folded_certificate_manifest_payload

Conditional.

The assembly rule for a two-cell manifest is proved in
`e1_two_cell_folded_manifest_assembly_soundness`. The remaining work is now
two explicit no-vector certificate leaves:

- `e1_folded_no_vector_certificate_128_payload`;
- `e1_folded_no_vector_certificate_256_payload`.

The common named field and primitive roots are already proved by
`e1_pocklington_250bit_exhibit_field`.
