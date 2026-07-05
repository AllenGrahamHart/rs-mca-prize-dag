# sov_affine_piece_partition_certificate_soundness

- **status:** PROVED
- **closure:** proof

## Statement

If a certificate partitions every forced-root conditioning cell into:

- disjoint affine pieces on which `c(L)=[X^{h-1}]L` has nonzero linear part;
  and
- paid or norm-structured exceptional pieces whose total size is below the
  declared character-sum budget;

then `sov_hminus1_affine_piece_decomposition` holds.

## Falsifier

A verified affine/exceptional partition certificate that fails to imply the
SOV `h-1` affine-piece decomposition.
