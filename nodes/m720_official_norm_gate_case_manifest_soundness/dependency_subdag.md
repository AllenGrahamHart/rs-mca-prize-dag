# dependency sub-DAG: m720_official_norm_gate_case_manifest_soundness

Edges are directed from dependency to consumer.

```text
m720_official_norm_gate_case_manifest_soundness [PROVED]
    -> m720_official_h7_20_norm_gate_payload [CONDITIONAL]
```

This proved node checks manifest coverage and accepted discharge types. It
does not construct the actual official case manifest; that is isolated in
`m720_official_norm_gate_case_manifest_payload`.
