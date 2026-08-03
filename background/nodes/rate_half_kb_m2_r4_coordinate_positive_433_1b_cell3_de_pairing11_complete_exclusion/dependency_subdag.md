# Dependency Sub-DAG

```text
(KBP1B3-CURVE-1): compact common curve and global kernel [PROVED]
                              |
                              v
       (KBP1B3-QUOT-1): global quadratic quotient [PROVED]
                              |
                              v
 (KBP1B3-DE-P11-1): pairing-11 common-f exclusion [PROVED]
                              |
                              v  evidence only
                    rate-half band [OPEN]
```

The quotient-to-pairing edge is `req`. The band edge is `ev`: this theorem
pays exactly 48 raw atlas cases and does not assert complete cell-3 closure.
