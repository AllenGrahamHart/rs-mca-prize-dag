# dependency sub-DAG: e1_folded_certificate_cell_256_payload

Edges are directed from dependency to consumer.

```text
e1_pocklington_250bit_exhibit_field [PROVED]
    -> e1_folded_certificate_cell_256_payload [CONDITIONAL]

e1_named_field_folded_cell_certificate_soundness [PROVED]
    -> e1_folded_certificate_cell_256_payload [CONDITIONAL]

e1_folded_no_vector_certificate_256_payload [TARGET]
    -> e1_folded_certificate_cell_256_payload [CONDITIONAL]

e1_folded_certificate_cell_256_payload [CONDITIONAL]
    -> e1_folded_certificate_manifest_payload [CONDITIONAL]
```

This conditional node supplies the `N'=256` transcript once the no-vector
certificate leaf is closed. The sibling conditional node
`e1_folded_certificate_cell_128_payload` supplies the other open E1 cell.
