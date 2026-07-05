# ATTACK - petal_kernel_realizable_sparsity

This is now an assembly node, not the live petal leaf.

The ambient kernel can grow linearly in `c`; literal flatness is refuted. The
proved node `petal_realizable_kernel_injection` reduces exact extras to
squarefree locator points inside the residue-line kernel.

Current reduction:

- `petal_squarefree_classification_counting_soundness` proves that a finite
  charged/uncharged classification with uniform polynomial bounds implies the
  required sparsity bound;
- `petal_squarefree_kernel_classification_payload` now reduces that
  classification to the actual ledger payload.

Further work should happen at `petal_squarefree_classification_ledger_payload`,
unless the conditional assembly here is found to be defective.
