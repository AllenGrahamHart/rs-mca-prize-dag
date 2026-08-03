# Dependency Sub-DAG

```text
(KBP1B3-CURVE-1): compact common curve and kernel [PROVED]
                              |
                              v
 (KBP1B3-QUOT-1): global quadratic quotient [PROVED]
                              |
                              v
 (KBP1B3-XI0P0-1): xi0/pairing0 outside exclusion [PROVED]
                              |
                              v
 (KBP1B3-XI1P0-1): parallel-edge transport [PROVED]
                              |
                              v
            remaining cell-3 outside ledger [OPEN]
                              |
                              v
              complete cell-3 exclusion [OPEN]
                              |
                              v
                    rate-half band [OPEN]
```

Both displayed child edges are `req`.  Edges to `rate_half_band_closure` are
evidence-only until every remaining cell-3 outside case and the downstream
composition are closed.
