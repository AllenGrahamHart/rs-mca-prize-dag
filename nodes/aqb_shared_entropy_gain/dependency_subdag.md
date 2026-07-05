# dependency sub-DAG: aqb_shared_entropy_gain

Edges are directed from dependency to consumer.

```text
aqb_family_certificate_semantics [PROVED]
    -> aqb_c2_average_family [CONDITIONAL]
    -> aqb_shared_entropy_gain_payload [TARGET]

aqb_c2_family_certificate_payload [TARGET]
    -> aqb_c2_average_family [CONDITIONAL]
    -> aqb_shared_entropy_gain_payload [TARGET]

aqb_c2_average_family [CONDITIONAL]
    -> aqb_shared_entropy_gain_payload [TARGET]
    -> aqb_shared_entropy_gain [CONDITIONAL]
    -> aqb_box_charge_amortization [CONDITIONAL]

aqb_entropy_ledger_certificate_soundness [PROVED]
    -> aqb_shared_entropy_gain [CONDITIONAL]
```

The open AQB entropy node is `aqb_shared_entropy_gain_payload`; it depends on
the concrete family certificate payload.
