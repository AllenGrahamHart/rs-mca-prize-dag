# proof: petal_squarefree_classification_ledger_soundness

Fix a coset-chart corridor cell and let `X` be the set of squarefree
realizable locator points inside the residue-line kernel.

The ledger gives disjoint records whose union is `X`. A charged record cites a
previously paid family, so those points are classified as charged and are not
part of the uncharged sparsity budget.

An uncharged record gives an explicit bound

```text
|C_i| <= K_i n^{A_i}
```

with exponent `A_i` independent of the excess `c`. The ledger also certifies
that the number of uncharged records is independent of `c`.

Therefore every point of `X` is classified either into a charged family or
into one of finitely many uncharged families with polynomial bounds whose
exponents are independent of `c`. This is exactly the classification required
by `petal_squarefree_kernel_classification_payload`.
