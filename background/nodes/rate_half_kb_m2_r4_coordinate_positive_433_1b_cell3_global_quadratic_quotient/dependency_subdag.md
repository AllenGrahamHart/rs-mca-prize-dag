# Dependency Sub-DAG

```text
(KBP1B3-CURVE-1): compact common curve and global kernel [PROVED]
                              |
                              v
       (KBP1B3-QUOT-1): global quadratic quotient [PROVED]
                              |
          +-------------+-------------+-------------+-------------+
          |             |             |             |             |
          v             v             v             v             v
 pairing-zero     (DE-FIRST-1)   (DE-P3/P4-1)   (DE-P5-1)    (DE-P6-1)
 packets [PROVED] 144 [PROVED]    96 [PROVED]    48 [PROVED]   48 [PROVED]
          |             |             |             |             |
          +-------------+-------------+-------------+-------------+
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

The displayed structural and exclusion edges are `req`.  The five aggregate
children pay matching indices zero through six for all parallel `DE`
missing copies.  Edges to `rate_half_band_closure` remain evidence-only until
the remaining outside ledger and complete cell-3 exclusion are proved.
