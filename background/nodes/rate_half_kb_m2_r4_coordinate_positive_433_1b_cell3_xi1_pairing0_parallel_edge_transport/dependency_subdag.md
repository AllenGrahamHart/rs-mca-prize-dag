# Dependency Sub-DAG

```text
(KBP1B3-QUOT-1): global quadratic quotient [PROVED]
                              |
                              v
 (KBP1B3-XI0P0-1): xi0/pairing0 exclusion [PROVED]
                              |
                              v
 (KBP1B3-XI1P0-1): parallel-edge transport [PROVED]
                              |
                              v
            remaining cell-3 outside ledger [OPEN]
                              |
                              v
                    rate-half band [OPEN]
```

The parent edge is `req`.  The rate-half edge is evidence-only until the
remaining outside ledger and downstream composition close.
