# dependency sub-DAG: aqb_entropy_ledger_certificate_soundness

Edges are directed from dependency to consumer.

```text
aqb_entropy_ledger_certificate_soundness [PROVED]
    -> aqb_shared_entropy_gain [CONDITIONAL]
```

This node proves only the monotone interval-arithmetic soundness rule. It does
not supply the concrete entropy ledger.
