# dependency sub-DAG: aqb_coupled_family_entropy_manifest_soundness

Edges are directed from dependency to consumer.

```text
aqb_family_certificate_semantics [PROVED]
    -> aqb_coupled_family_entropy_manifest_soundness [PROVED]
    -> aqb_c2_family_certificate_payload [CONDITIONAL]

aqb_entropy_ledger_certificate_soundness [PROVED]
    -> aqb_coupled_family_entropy_manifest_soundness [PROVED]
    -> aqb_shared_entropy_gain_payload [CONDITIONAL]

aqb_coupled_family_entropy_manifest_payload [TARGET]
    -> aqb_c2_family_certificate_payload [CONDITIONAL]
    -> aqb_c2_average_family [CONDITIONAL]

aqb_coupled_family_entropy_manifest_payload [TARGET]
    -> aqb_shared_entropy_gain_payload [CONDITIONAL]
    -> aqb_shared_entropy_gain [CONDITIONAL]
```

This node proves only coupled-manifest semantics. The actual family and ledger
are supplied by the payload node.
