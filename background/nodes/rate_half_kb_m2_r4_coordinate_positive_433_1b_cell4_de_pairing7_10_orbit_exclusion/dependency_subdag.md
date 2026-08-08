# Dependency Sub-DAG

```mermaid
graph LR
  P[Pairing-7 complete exclusion] --> O[Pairing-7/10 orbit exclusion]
  Q[Parallel-DE matching quotient] --> O
  C[Previous 27-label complete block] --> O
  O -. evidence .-> R[Rate-half band closure]
```

The prior complete block is required only for the cumulative 31-label
ledger; the four-label orbit exclusion itself uses the first two parents.
