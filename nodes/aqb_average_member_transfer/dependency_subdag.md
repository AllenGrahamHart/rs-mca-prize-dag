# dependency sub-DAG: aqb_average_member_transfer

Edges are directed from dependency to consumer.

```text
aqb_average_member_transfer [PROVED]
    -> rate_half_band_closure [CONDITIONAL]
```

This node is purely the finite average-to-member implication. The actual
averaged family and its entropy gain remain in `aqb_c2_average_family` and
`aqb_shared_entropy_gain`.
