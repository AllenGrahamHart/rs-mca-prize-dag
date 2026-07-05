# conditional: petal_kernel_realizable_sparsity

This node is conditional on:

- `petal_squarefree_classification_counting_soundness`
- `petal_squarefree_kernel_classification_payload`

The first dependency is proved. The second is now conditional on the live
classification ledger payload: it must classify squarefree realizable locator
points inside residue-line kernels into charged classes and uniformly
polynomial uncharged classes, with a number of uncharged classes independent
of the excess `c`.
