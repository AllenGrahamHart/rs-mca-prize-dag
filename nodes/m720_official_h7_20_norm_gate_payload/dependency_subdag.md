# dependency sub-DAG: m720_official_h7_20_norm_gate_payload

Edges are directed from dependency to consumer.

```text
m720_official_norm_gate_case_manifest_soundness [PROVED]
    -> m720_official_h7_20_norm_gate_payload [CONDITIONAL]

m720_official_norm_gate_case_manifest_payload [TARGET]
    -> m720_official_h7_20_norm_gate_payload [CONDITIONAL]
    -> m720_official_h7_20_norm_gate_certificates [CONDITIONAL]
    -> m720_official_exclusion [CONDITIONAL]
```

The open node is now `m720_official_norm_gate_case_manifest_payload`: the
actual official primitive norm-gate case manifest.
