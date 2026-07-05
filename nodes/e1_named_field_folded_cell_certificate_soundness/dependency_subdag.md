# dependency sub-DAG: e1_named_field_folded_cell_certificate_soundness

Edges are directed from dependency to consumer.

```text
e1_named_field_folded_cell_certificate_soundness [PROVED]
    -> e1_folded_certificate_cell_128_payload [CONDITIONAL]
    -> e1_folded_certificate_cell_256_payload [CONDITIONAL]
```

This node is the schema-dispatch rule converting a named field plus a complete
zero no-vector certificate into an E1 cell payload.
