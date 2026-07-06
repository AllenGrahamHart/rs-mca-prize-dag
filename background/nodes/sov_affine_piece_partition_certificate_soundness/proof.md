# proof: sov_affine_piece_partition_certificate_soundness

Fix an official-shape row, `h in (20,A]`, and a forced-root
higher-coefficient conditioning cell `Omega`.

The certificate gives a disjoint partition of `Omega` into affine pieces
`P_alpha` and exceptional pieces `E_beta`. On each `P_alpha`, the coefficient
map

```text
c(L) = [X^{h-1}]L
```

is certified affine-linear with nonzero linear part. The exceptional pieces
are certified paid or norm-structured, and their total size is below the
declared character-sum budget.

This is exactly the decomposition asserted by
`sov_hminus1_affine_piece_decomposition`: every conditioned cell is covered by
cancellative affine pieces plus budget-small paid/norm-structured exceptions.
Since the argument applies to every row, `h`, and conditioning cell, the node
holds.
