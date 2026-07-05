# conditional: petal_squarefree_kernel_classification_payload

## Predicate nodes

- `petal_squarefree_classification_ledger_soundness`
- `petal_squarefree_classification_ledger_payload`

## Claim

Conditional on the actual squarefree classification ledger, the squarefree
kernel classification payload holds.

## Proof

The predicate `petal_squarefree_classification_ledger_payload` supplies a
ledger covering every squarefree realizable locator point inside the
residue-line kernels. Each record is either charged, with a citation to the
ledger that pays it, or uncharged, with a polynomial bound whose exponent is
independent of the excess `c`. The payload also bounds the number of
uncharged records independently of `c`.

The proved predicate `petal_squarefree_classification_ledger_soundness` says
that such a complete ledger implies exactly the charged/uncharged
classification required here. Therefore this node follows from the actual
ledger payload.
