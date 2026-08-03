# Dependency Sub-DAG

```text
(KBP1B3-CURVE-1): compact common curve and global kernel [PROVED]
                              |
                              v
       (KBP1B3-QUOT-1): global quadratic quotient [PROVED]
                              |
          + pairing-zero packets [PROVED]
          + DE-FIRST-1: 144 [PROVED]
          + DE-P3/P4-1: 96 [PROVED]
          + DE-P5-1: 48 [PROVED]
          + DE-P6-1: 48 [PROVED]
          + DE-P7-1: 48 [PROVED]
          + DE-P8-1: 48 [PROVED]
          + DE-P9-1: 48 [PROVED]
          + DE-P10-1: 48 [PROVED]
          + DE-P11-1: 48 [PROVED]
          + DE-P12-1: 48 [PROVED]
          + DE-P13-1: 48 [PROVED]
          + DE-P14-1: 48 [PROVED]
                              |
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

The displayed structural and exclusion edges are `req`.  The thirteen aggregate
children pay matching indices zero through fourteen for all parallel `DE`
missing copies.  Edges to `rate_half_band_closure` remain evidence-only until
the remaining outside ledger and complete cell-3 exclusion are proved.
