# dependency sub-DAG: petal_squarefree_classification_ledger_soundness

Edges are directed from dependency to consumer.

```text
petal_squarefree_classification_ledger_soundness [PROVED]
    -> petal_squarefree_kernel_classification_payload [CONDITIONAL]
```

This proved node checks the ledger format. It does not construct the actual
Petal classification ledger; that is isolated in
`petal_squarefree_classification_ledger_payload`.
