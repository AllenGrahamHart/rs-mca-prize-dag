# Dependency Sub-DAG

```text
positive 433-1b signed-edge atlas                 [PROVED]
cell-4 xi0/pairing0 four-basis exclusion          [PROVED]
                               |
                               v
cell-4 xi1/pairing0 parallel-edge transport       [PROVED]
                               |
                               v
remaining cell-4 outside ledger                    [OPEN]
                               |
                               v
rate-half band                                     [OPEN]
```

The parent and atlas edges are `req`.  The rate-half edge is evidence-only
until the remaining outside ledger and downstream composition close.
