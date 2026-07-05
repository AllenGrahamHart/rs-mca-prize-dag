# ATTACK - sov_hminus1_character_sum_bound

This node is now an assembly point.

The generic fiber-to-character-sum reduction is proved in
`sov_hminus1_fiber_fourier_duality`. The generic cancellation over
nonconstant affine pieces is proved in
`sov_nonconstant_affine_character_cancellation`. The remaining task is
specific to the anchored-core family and the forced-root conditioning.

The active leaf is `sov_affine_piece_partition_payload`:

- decompose conditioned anchored-core cells into affine pieces where the
  `h-1` elementary-symmetric coefficient has nonzero linear part;
- show that any non-cancellative piece is norm-structured, paid, or below the
  character-sum budget;
- classify constant-coefficient conditioned families and prove they are empty
  or already charged.

Sampling evidence is not a proof.
