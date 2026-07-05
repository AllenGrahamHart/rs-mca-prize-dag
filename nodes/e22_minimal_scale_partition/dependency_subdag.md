# dependency sub-DAG: e22_minimal_scale_partition

Edges are directed from dependency to consumer.

```text
e22_dyadic_minimal_scale_selector [PROVED]
    -> e22_minimal_scale_partition [PROVED]
    -> e22_minimal_scale_count_formula [CONDITIONAL]

e22_minimal_scale_tail_criterion [PROVED]
    -> e22_minimal_scale_partition [PROVED]
```

The proved node supplies only the disjoint partition by selected minimal
scale. It does not evaluate the dyadic pricing column.
