# petal_squarefree_kernel_classification_payload

- **status:** CONDITIONAL
- **closure:** proof

## Statement

Across the coset-chart corridor, classify the squarefree locator points inside
the residue-line kernels that correspond to exact full-petal extras into:

- charged families already paid elsewhere; and
- uncharged families with polynomial bounds whose exponents are independent
  of the excess `c`.

The number of uncharged families must also be bounded independently of `c`.

This is reduced to:

- `petal_squarefree_classification_ledger_soundness`, which proves that a
  complete charged/uncharged classification ledger implies this payload; and
- `petal_squarefree_classification_ledger_payload`, which remains to
  construct the actual squarefree classification ledger.

## Falsifier

An unclassified squarefree realizable kernel family, or an uncharged family
whose size requires an exponent growing with `c`.
