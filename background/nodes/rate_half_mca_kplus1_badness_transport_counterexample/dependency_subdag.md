# Dependency sub-DAG

```text
rate_half_mca_kplus1_badness_transport_counterexample [PROVED]
  --ev--> mca_safe [CONDITIONAL]
```

The proof is direct and imports no mathematical dependency.  The outgoing
edge is evidence only: it constrains the witness adapter used by candidate
safe-side routes and proves no safe bound.
