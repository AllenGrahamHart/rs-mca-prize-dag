# Dependency Sub-DAG

```text
(KBP1B3-CURVE-1): compact common curve and global kernel [PROVED]
                              |
                              v
       (KBP1B3-QUOT-1): global quadratic quotient [PROVED]
                              |
                              v
 (KBP1B3-XI6-ENDPOINT-1): xi6 source compatibility exclusion [PROVED]
                              |
                              v  evidence only
                    rate-half band [OPEN]
```

The quotient-to-exclusion edge is `req`. The band edge is `ev`: this theorem
pays exactly 240 raw atlas cases and does not assert complete cell-3 closure.
