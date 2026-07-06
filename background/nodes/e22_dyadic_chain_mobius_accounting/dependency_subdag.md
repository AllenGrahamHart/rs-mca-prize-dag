# dependency sub-DAG: e22_dyadic_chain_mobius_accounting

Edges are directed from dependency to consumer.

```text
e22_minimal_scale_partition [PROVED]
    -> e22_dyadic_chain_mobius_accounting [PROVED]
    -> e22_minimal_scale_column_evaluation [CONDITIONAL]
```

The proved node is only formal triangular accounting. It leaves the overlap
counts to `e22_minimal_scale_overlap_counts`.
