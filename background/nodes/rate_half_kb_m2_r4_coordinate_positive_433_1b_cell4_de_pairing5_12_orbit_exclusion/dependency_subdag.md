# Dependency Sub-DAG

```mermaid
graph LR
  P[Pairing-5 complete exclusion] --> O[Pairing-5/12 orbit exclusion]
  Q[Parallel-DE matching quotient] --> O
  C[Previous 21-label complete block] --> O
  O -. evidence .-> R[Rate-half band closure]
```

The prior complete block is required only for the cumulative 25-label
ledger; the four-label orbit exclusion itself uses the first two parents.
