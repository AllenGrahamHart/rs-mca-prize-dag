# dependency sub-DAG: petal_squarefree_kernel_classification_payload

Edges are directed from dependency to consumer.

```text
petal_squarefree_classification_ledger_soundness [PROVED]
    -> petal_squarefree_kernel_classification_payload [CONDITIONAL]

petal_squarefree_classification_ledger_payload [TARGET]
    -> petal_squarefree_kernel_classification_payload [CONDITIONAL]
    -> petal_kernel_realizable_sparsity [CONDITIONAL]
    -> petal_realizable_extra_uniformity [CONDITIONAL]
```

The open node is now `petal_squarefree_classification_ledger_payload`: the
actual charged/uncharged structural ledger.
