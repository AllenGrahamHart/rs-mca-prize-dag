# Dependency Sub-DAG

```mermaid
graph LR
  P[Pairing-4 complete exclusion] --> O[Pairing-4/9 orbit exclusion]
  Q[Parallel-DE matching quotient] --> O
  C[Previous 15-label complete block] --> O
  O -. evidence .-> R[Rate-half band closure]
```

The prior complete block is required only for the cumulative 19-label
ledger; the four-label orbit exclusion itself uses the first two parents.
