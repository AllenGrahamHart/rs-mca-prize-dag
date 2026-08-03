# Dependency Sub-DAG

```text
 (KBP1B3-XI0P0-1) [PROVED] ----+
                                  |
 (KBP1B3-XI1P0-1) [PROVED] ----+----> (KBP1B3-DE-FIRST-1) [PROVED]
                                  |                    |
 (KBP1B3-XI2P0-1) [PROVED] ----+                    v
                                           remaining cell-3 ledger [OPEN]
                                                        |
                                                        v
                                              rate-half band [OPEN]
```

All three parent edges are `req`.  The rate-half edge is evidence-only until
the remaining outside ledger and downstream composition close.
