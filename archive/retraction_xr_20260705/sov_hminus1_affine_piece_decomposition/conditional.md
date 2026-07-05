# conditional: sov_hminus1_affine_piece_decomposition

This node is conditional on:

- `sov_nonconstant_affine_character_cancellation`
- `sov_affine_piece_partition_certificate_soundness`
- `sov_affine_piece_partition_payload`

The first two dependencies are proved. The live payload must construct the
actual anchored-core partitions into cancellative affine pieces plus
budget-small paid/norm-structured exceptions.
