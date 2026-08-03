# Dependency Sub-DAG

```text
(KBP1B3-CURVE-1): compact common curve and kernel [PROVED]
                              |
                              v
(KBP1B3-QUOT-1): global quadratic quotient [PROVED]
                              |
                              v
(KBP1B3-DE-P4-1): pairing-4 DE block [PROVED]
                              |
                              v
             remaining cell-3 outside ledger [OPEN]
                              |
                              v
                  complete cell-3 exclusion [OPEN]
                              |
                              v
                       rate-half band [OPEN]
```

The quotient-to-pairing-4 edge is `req`.  The edge to
`rate_half_band_closure` is evidence-only until every remaining cell-3
outside case and the other rate-half obligations are proved.
