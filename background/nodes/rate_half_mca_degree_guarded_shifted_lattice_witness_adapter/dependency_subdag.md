# Dependency sub-DAG

```text
one-shift lattice/support census [upstream PROVED]
K-to-K+1 mutation              [local PROVED necessity control]
                  |
                  v
degree-guarded shifted-lattice witness adapter [PROVED]
                  |
                  +--ev--> mca_safe [CONDITIONAL]
```

The proof is direct; the first two entries provide source alignment and a
necessity control rather than hidden assumptions.  The outgoing edge is
evidence only and supplies no safe-side bound.
