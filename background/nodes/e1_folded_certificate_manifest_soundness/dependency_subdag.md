# dependency sub-DAG: e1_folded_certificate_manifest_soundness

Edges are directed from dependency to consumer.

```text
e1_folded_certificate_manifest_soundness [PROVED]
    -> e1_open_cell_control_payload [CONDITIONAL]
```

This proved node checks coverage and route shape for named folded-certificate
manifests. It does not supply the actual E1 certificate transcripts.
