# dependency sub-DAG: e1_folded_certificate_manifest_payload

Edges are directed from dependency to consumer.

```text
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
```

This node assembles the two project-specific folded certificates for the E1
open cells. The remaining live leaves are the no-vector payloads; the common
field is already proved.
