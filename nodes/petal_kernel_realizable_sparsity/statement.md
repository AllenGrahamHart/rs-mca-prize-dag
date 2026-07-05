# petal_kernel_realizable_sparsity

- **status:** CONDITIONAL
- **closure:** proof

## Statement

Across the coset-chart corridor, the squarefree locator points inside the
residue-line kernel

```text
K_{I,d} = ker(pi_{>d} R_{I,d})
```

that correspond to exact full-petal extras are bounded by a polynomial whose
exponent is independent of the excess `c`.

This node is now reduced to:

- `petal_squarefree_classification_counting_soundness`, the proved finite
  classification-to-sparsity counting rule; and
- `petal_squarefree_kernel_classification_payload`, the remaining structural
  classification of squarefree realizable kernel points.

## Falsifier

A corridor family where squarefree realizable locator points inside the
residue-line kernel grow beyond the uniform polynomial budget as `c`
increases despite the asserted squarefree-kernel classification.
