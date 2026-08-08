# Dependency Sub-DAG

```text
(KBP1B4-TOWER-1): guarded four-basis source tower [PROVED]
                              |
                              v
(KBP1B-O0A-ATLAS-1): deployed signed-edge atlas [PROVED]
                              |
                              v
(KBP1B4-DE-P3-1): pairing-3 DE block [PROVED]
                              |
                              v
              matching-orbit composition [OPEN HERE]
                              |
                              v
                 remaining cell-4 ledger [OPEN]
                              |
                              v
                    rate-half band [OPEN]
```

The tower and atlas edges are `req`. The edge to
`rate_half_band_closure` is evidence-only until all remaining cell-4 and
rate-half obligations are proved.
