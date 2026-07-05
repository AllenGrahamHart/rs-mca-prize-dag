# e22_common_tail_invariance_certificate_soundness

- **status:** PROVED
- **closure:** proof

## Statement

Suppose an E22 cofactor-tail certificate supplies:

- one common tail `B`;
- dyadic local moduli `M_i>t`;
- a verified bound `|B| < min_i M_i`;
- for every touched petal, a verified proof that `T_i \ B` is invariant under
  the `M_i`-th-root kernel of `x -> x^{M_i}`.

Then `e22_cofactor_common_tail_kernel_invariance` holds.

## Falsifier

A certificate verifying all four fields but failing to imply the common-tail
kernel-invariance predicate.
