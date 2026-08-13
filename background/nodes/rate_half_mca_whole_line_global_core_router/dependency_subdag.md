# Dependency sub-DAG

```text
common-core cancellation/staircase import [PROVED] --------+
record-local core owner noninvariance [PROVED route cut] ---+
                                                            v
whole-line global-core cancellation router [PROVED]
                                                            |
                                                            +--ev--> rate_half_band_crossing_location [TARGET]
```

The first input supplies the reversible cancellation and exact payment
walls. The second is the hostile control that forces line-global ownership.
The outgoing edge is evidence only: the shortened residual remains open.
