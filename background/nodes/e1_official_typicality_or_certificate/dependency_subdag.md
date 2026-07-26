# dependency sub-DAG: e1_official_typicality_or_certificate

Edges are directed from dependency to consumer.

```text
official_row_primes_pinning [PROVED]
    -> e1_open_cell_route_soundness [PROVED]
    -> e1_official_typicality_or_certificate [CONDITIONAL]
    -> e1_official_prime_exception_control [CONDITIONAL]

e1_folded_certificate_soundness [PROVED]
    -> e1_open_cell_route_soundness [PROVED]

e1_folded_certificate_manifest_soundness [PROVED]
    -> e1_open_cell_control_payload [CONDITIONAL]

e1_two_cell_folded_manifest_assembly_soundness [PROVED]
    -> e1_folded_certificate_manifest_payload [CONDITIONAL]

e1_pocklington_250bit_exhibit_field [PROVED]
    -> e1_folded_certificate_cell_128_payload [CONDITIONAL]
    -> e1_folded_certificate_cell_256_payload [CONDITIONAL]

e1_named_field_folded_cell_certificate_soundness [PROVED]
    -> e1_folded_certificate_cell_128_payload [CONDITIONAL]
    -> e1_folded_certificate_cell_256_payload [CONDITIONAL]

e1_folded_no_vector_certificate_128_payload [TARGET]
    -> e1_folded_certificate_cell_128_payload [CONDITIONAL]

e1_folded_no_vector_certificate_256_payload [TARGET]
    -> e1_folded_certificate_cell_256_payload [CONDITIONAL]

e1_folded_certificate_cell_128_payload [CONDITIONAL]
    -> e1_folded_certificate_manifest_payload [CONDITIONAL]

e1_folded_certificate_cell_256_payload [CONDITIONAL]
    -> e1_folded_certificate_manifest_payload [CONDITIONAL]

e1_folded_certificate_manifest_payload [CONDITIONAL]
    -> e1_open_cell_control_payload [CONDITIONAL]

e1_open_cell_control_payload [CONDITIONAL]
    -> e1_official_typicality_or_certificate [CONDITIONAL]
```

The open E1 targets are now the two folded no-vector certificate payloads, not
route dispatch, field selection, or folded-certificate semantics.
