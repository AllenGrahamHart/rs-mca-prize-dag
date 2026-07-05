# dependency sub-DAG: m720_official_h7_20_norm_gate_certificates

Edges are directed from dependency to consumer.

```text
m720_certificate_semantics [PROVED]
    -> m720_official_norm_gate_certificate_soundness [PROVED]
    -> m720_official_h7_20_norm_gate_certificates [CONDITIONAL]
    -> m720_official_exclusion [CONDITIONAL]

m720_official_paid_branch_alignment [PROVED]
    -> m720_official_norm_gate_certificate_soundness [PROVED]

m720_official_norm_gate_case_manifest_soundness [PROVED]
    -> m720_official_h7_20_norm_gate_payload [CONDITIONAL]

m720_official_norm_gate_case_manifest_payload [TARGET]
    -> m720_official_h7_20_norm_gate_payload [CONDITIONAL]
    -> m720_official_h7_20_norm_gate_certificates [CONDITIONAL]

m720_official_h7_20_norm_gate_payload [CONDITIONAL]
    -> m720_official_h7_20_norm_gate_certificates [CONDITIONAL]
```

The open node is `m720_official_norm_gate_case_manifest_payload`.
