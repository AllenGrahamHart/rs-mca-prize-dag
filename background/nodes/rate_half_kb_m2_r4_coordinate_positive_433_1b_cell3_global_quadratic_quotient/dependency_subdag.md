# Dependency Sub-DAG

```text
(KBP1B3-CURVE-1): compact common curve and global kernel [PROVED]
                              |
                              v
       (KBP1B3-QUOT-1): global quadratic quotient [PROVED]
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
  pairing-zero packets   (KBP1B3-DE-P3-1)  (KBP1B3-DE-P4-1)
       [PROVED]            48 cases [PROVED]    48 cases [PROVED]
          |
          v
 (KBP1B3-DE-FIRST-1): 144 cases [PROVED]
          |                   |                   |
          +-------------------+-------------------+
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

The displayed structural and exclusion edges are `req`.  The three aggregate
children pay matching indices zero through four for all parallel `DE`
missing copies.  Edges to `rate_half_band_closure` remain evidence-only until
the remaining outside ledger and complete cell-3 exclusion are proved.
