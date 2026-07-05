# frontier: petal_realizable_extra_uniformity

Conditional.

The Modal helper can count exact realizable full-petal extras on calibration
rows, but this working copy has no complete proof that those counts remain
within the uniform polynomial budget as `c` grows.

The injection into squarefree locator points inside the residue-line kernel is
proved by `petal_realizable_kernel_injection`. The old sparsity target
`petal_kernel_realizable_sparsity` has been split. The active target is now
`petal_squarefree_kernel_classification_payload`.

Tiny local diagnostic, not proof: for the coset row `p=31, ell=3, t=5` with
sequential scalars and the Modal helper's capped core pool, exact realizable
extras over `c=1..7` are

```text
0, 0, 0, 0, 0, 2, 12.
```

This is consistent with the corrected route: the ambient kernel dimension
grows, but the exact realizable subset is much smaller. A proof must classify
that subset uniformly.
