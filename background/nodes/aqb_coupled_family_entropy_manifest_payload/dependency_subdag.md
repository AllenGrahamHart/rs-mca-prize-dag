# dependency sub-DAG: aqb_coupled_family_entropy_manifest_payload

Edges are directed from dependency to consumer.

```text
aqb_coupled_family_entropy_manifest_payload [TARGET]
    -> aqb_c2_family_certificate_payload [CONDITIONAL]
    -> aqb_c2_average_family [CONDITIONAL]
    -> aqb_averaged_quotient_box [CONDITIONAL]

aqb_coupled_family_entropy_manifest_payload [TARGET]
    -> aqb_shared_entropy_gain_payload [CONDITIONAL]
    -> aqb_shared_entropy_gain [CONDITIONAL]
    -> aqb_box_charge_amortization [CONDITIONAL]
```

This target supplies both the actual family certificate and the entropy
ledger for that same family.
