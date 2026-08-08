# Dependency Sub-DAG

```mermaid
graph LR
  P[Pairing-8 complete exclusion] --> O[Pairing-8/13 orbit exclusion]
  Q[Parallel-DE matching quotient] --> O
  C[Previous 33-label complete block] --> O
  O -. evidence .-> R[Rate-half band closure]
```

The prior complete block is required only for the cumulative 37-label
ledger; the four-label orbit exclusion itself uses the first two parents.
