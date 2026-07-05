# ATTACK - sov_hminus1_affine_piece_decomposition

This is now an assembly node. The live SOV character-sum leaf is
`sov_affine_piece_partition_payload`.

The formal affine cancellation lemma and partition-certificate soundness are
proved. What remains is specific to anchored cores under the forced-root
conditioning:

- describe the conditioned anchored-core solution set by local coordinates;
- find affine directions along which `[X^{h-1}]L` has nonzero linear part;
- partition away singular, norm-structured, or paid pieces;
- prove the total size of the exceptional pieces is below the active-core
  character-sum budget.

This node may also be closed by a different structural theorem if it implies
the same decomposition: all large constant-coefficient components are paid or
below budget.
