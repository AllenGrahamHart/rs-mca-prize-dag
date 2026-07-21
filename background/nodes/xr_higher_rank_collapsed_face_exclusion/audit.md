# Audit

- The active trade support `S_i` need only be contained in the selected
  agreement block. Equality is unnecessary; containment supplies all
  `a+1` interpolation points.
- Polynomial uniqueness is applied after the one common coordinate scaling
  has normalized the kernel to `GRS_a`. Using unrelated block scalings would
  invalidate `(CFE2)`.
- The contradiction uses actual selected-error zero sets, not only chosen
  agreement subsets. Once polynomial equality extends an agreement to `X`,
  the post-strip cap applies to it.
- The exact common set has size at least `k+2`; calling this merely a
  near-tangent defect discards the stronger pairwise-core contradiction.
- The argument needs two active rows; rank-two trades have at least four.
- Larger active unions are not facet systems and are not removed by this
  proof.
