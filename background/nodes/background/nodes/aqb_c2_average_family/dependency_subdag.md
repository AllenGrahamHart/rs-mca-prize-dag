# dependency sub-DAG: aqb_c2_average_family

Edges are directed from dependency to consumer.

```text
aqb_family_certificate_semantics [PROVED]
    -> aqb_c2_average_family [CONDITIONAL]
    -> aqb_averaged_quotient_box [CONDITIONAL]

aqb_c2_family_certificate_payload [TARGET]
    -> aqb_c2_average_family [CONDITIONAL]
```

The open AQB family target is now the concrete certificate payload. This node
records only the conditional assembly from a verified certificate to the
family-existence predicate.
