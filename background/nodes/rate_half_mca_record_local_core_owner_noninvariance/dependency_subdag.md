# Dependency sub-DAG

```text
same-record common-core cancellation adapter [PROVED upstream import]
                         |
                         | interpretation only
                         v
record-local core owner noninvariance [PROVED]
                         |
                         +--ev--> rate_half_band_crossing_location [TARGET]
```

The finite theorem is proved directly. The imported adapter explains why
both cores remain legitimate cancellation inputs; it is not a hidden proof
assumption. The outgoing edge is evidence about the route architecture only.
