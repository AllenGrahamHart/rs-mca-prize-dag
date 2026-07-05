# sov_hminus1_affine_piece_decomposition

- **status:** CONDITIONAL
- **closure:** proof

## Statement

For every official-shape row, every `h in (20,A]`, and every forced-root
higher-coefficient conditioning cell of anchored-core locators, partition the
cell into:

- affine pieces on which

  ```text
  c(L) = [X^{h-1}]L
  ```

  is nonconstant affine-linear; and
- exceptional paid or norm-structured pieces whose total size is below the
  character-sum budget needed by `sov_hminus1_fiber_fourier_duality`.

This node is reduced to:

- `sov_affine_piece_partition_certificate_soundness`, the proved soundness
  rule for affine/exceptional partition certificates; and
- `sov_affine_piece_partition_payload`, the remaining anchored-core partition
  construction.

## Falsifier

A conditioning cell with a large non-paid component on which the `h-1`
coefficient is constant or has no cancellative affine direction, or a defect
in the partition certificate soundness rule.
