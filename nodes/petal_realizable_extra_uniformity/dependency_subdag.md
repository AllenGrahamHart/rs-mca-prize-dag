# dependency sub-DAG: petal_realizable_extra_uniformity

```text
l1_coset_chart_residue_bridge [PROVED]
    -> petal_realizable_kernel_injection [PROVED]
    -> petal_realizable_extra_uniformity [CONDITIONAL]
    -> petal_residue_line_uniformity [CONDITIONAL]

petal_squarefree_classification_counting_soundness [PROVED]
    -> petal_kernel_realizable_sparsity [CONDITIONAL]
    -> petal_realizable_extra_uniformity [CONDITIONAL]

petal_squarefree_classification_ledger_payload [TARGET]
    -> petal_squarefree_kernel_classification_payload [CONDITIONAL]
    -> petal_kernel_realizable_sparsity [CONDITIONAL]
    -> petal_realizable_extra_uniformity [CONDITIONAL]

petal_squarefree_kernel_classification_payload [CONDITIONAL]
    -> petal_kernel_realizable_sparsity [CONDITIONAL]
    -> petal_realizable_extra_uniformity [CONDITIONAL]
```

The old realizable-extra leaf has been split into:

- a proved injection/reduction to squarefree locator points in the kernel; and
- a conditional sparsity theorem for those points, whose remaining leaf is
  `petal_squarefree_classification_ledger_payload`.
