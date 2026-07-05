# dependency sub-DAG: petal_kernel_realizable_sparsity

```text
l1_coset_chart_residue_bridge [PROVED]
    -> petal_realizable_kernel_injection [PROVED]
    -> petal_realizable_extra_uniformity [CONDITIONAL]

petal_squarefree_classification_counting_soundness [PROVED]
    -> petal_kernel_realizable_sparsity [CONDITIONAL]
    -> petal_realizable_extra_uniformity [CONDITIONAL]

petal_squarefree_classification_ledger_soundness [PROVED]
    -> petal_squarefree_kernel_classification_payload [CONDITIONAL]

petal_squarefree_classification_ledger_payload [TARGET]
    -> petal_squarefree_kernel_classification_payload [CONDITIONAL]
    -> petal_kernel_realizable_sparsity [CONDITIONAL]

petal_squarefree_kernel_classification_payload [CONDITIONAL]
    -> petal_kernel_realizable_sparsity [CONDITIONAL]
```

The open Petal sparsity target is now the squarefree classification ledger
payload. This node records only the conditional assembly from that ledger to
uniform sparsity.
