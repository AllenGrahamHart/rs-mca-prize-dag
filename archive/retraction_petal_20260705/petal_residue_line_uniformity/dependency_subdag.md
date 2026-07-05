# dependency sub-DAG: petal_residue_line_uniformity

Edges are directed from dependency to consumer.

```text
l1_coset_chart_residue_bridge [PROVED]
    -> petal_residue_kernel_linear_bound [PROVED]
    -> petal_residue_line_uniformity

l1_defect_layer_bounds [PROVED]
    -> petal_residue_kernel_linear_bound [PROVED]

petal_residue_kernel_linear_bound [PROVED]
    -> petal_residue_kernel_flatness [REFUTED route]

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

petal_squarefree_kernel_classification_payload [CONDITIONAL]
    -> petal_kernel_realizable_sparsity [CONDITIONAL]
```

## Status

- `petal_residue_kernel_linear_bound`: PROVED. This records Lemma 13,
  `dim K <= c+1`.
- `petal_residue_kernel_flatness`: REFUTED as literal ambient-dimension
  flatness. Tiny coset rows have `dim K` growing with `c`.
- `petal_realizable_extra_uniformity`: CONDITIONAL. The injection into kernel
  locator points is proved, and the sparsity step is conditional.
- `petal_kernel_realizable_sparsity`: CONDITIONAL. The finite-union counting
  consequence is proved.
- `petal_squarefree_classification_ledger_payload`: TARGET. This asks for the
  structural squarefree-kernel classification ledger that supplies the
  remaining sparsity payload.
- `petal_residue_line_uniformity`: CONDITIONAL on the proved linear bound and
  the realizable-extra target.
