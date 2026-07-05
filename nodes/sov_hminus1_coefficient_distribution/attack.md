# ATTACK - sov_hminus1_coefficient_distribution

This node is now an assembly node.

The algebraic sensitivity of the obstruction is already proved in
`sov_first_obstruction_sensitivity`: changing `[X^{h-1}]L` changes
`O_{h-1}` by `-1` while leaving the forced root fixed. The generic
finite-Fourier reduction from coefficient fibers to nontrivial additive
character sums is now proved in `sov_hminus1_fiber_fourier_duality`.

The remaining problem is `sov_affine_piece_partition_payload`: decompose
the conditioned anchored-core cells into cancellative affine pieces plus
budget-small paid/norm-structured exceptions.

Possible routes:

- affine-piece cancellation for the `h-1` elementary-symmetric coefficient on
  the conditioned anchored-core family;
- a norm-structure argument showing large coefficient fibers are paid;
- a structural classification of constant-coefficient families, showing they
  are impossible or already charged.

Sampling evidence is not a proof.
