# Dependency Sub-DAG

```text
(KBP1B3-CURVE-1): compact common curve and kernel [PROVED]
                              |
                              v
 (KBP1B3-QUOT-1): global quadratic quotient [PROVED]
                              |
                              v
 (KBP1B3-XI2P0-1): xi2/pairing0 exclusion [PROVED]
                              |
                              v
            remaining cell-3 outside ledger [OPEN]
                              |
                              v
                    rate-half band [OPEN]
```

The parent edge is `req`.  The rate-half edge is evidence-only until the
remaining outside ledger and downstream composition close.
