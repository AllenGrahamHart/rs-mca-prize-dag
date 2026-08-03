# Dependency Sub-DAG

```text
(KBP1B3-CURVE-1): compact common curve and global kernel [PROVED]
                              |
                              v
       (KBP1B3-QUOT-1): global quadratic quotient [PROVED]
                              |
             +----------------+----------------+----------------+
             |                                 |                |
             v                                 v                |
 (KBP1B3-XI0P0-1) [PROVED]        (KBP1B3-XI2P0-1) [PROVED]
             |
             v
 (KBP1B3-XI1P0-1) [PROVED]
             |                                 |
             +----------------+----------------+
                              |
                              v
 (KBP1B3-DE-FIRST-1): 144-case first-pair block [PROVED]
                                                               |
                                                               v
                                  (KBP1B3-DE-P3-1): 48 cases [PROVED]
                              |                                |
                              +---------------+----------------+
                                              |
                                              v
          remaining pair-algebra outside ledger [OPEN]
                              |
                              v
              complete cell-3 exclusion [OPEN]
                              |
                              v
                    rate-half band [OPEN]
```

The displayed structural and exclusion edges are `req`.  The two aggregate
children pay matching indices zero through three for all parallel `DE`
missing copies.  Edges to `rate_half_band_closure` remain evidence-only until
the remaining outside ledger and complete cell-3 exclusion are proved.
