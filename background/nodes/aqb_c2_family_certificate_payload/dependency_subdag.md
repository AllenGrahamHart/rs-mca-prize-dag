# dependency sub-DAG: aqb_c2_family_certificate_payload

Edges are directed from dependency to consumer.

```text
aqb_family_certificate_semantics [PROVED]
    -> aqb_coupled_family_entropy_manifest_soundness [PROVED]
    -> aqb_c2_family_certificate_payload [CONDITIONAL]
    -> aqb_c2_average_family [CONDITIONAL]

aqb_entropy_ledger_certificate_soundness [PROVED]
    -> aqb_coupled_family_entropy_manifest_soundness [PROVED]

aqb_coupled_family_entropy_manifest_payload [TARGET]
    -> aqb_c2_family_certificate_payload [CONDITIONAL]
```

This node is now an assembly from coupled-manifest soundness plus the actual
coupled AQB manifest.
