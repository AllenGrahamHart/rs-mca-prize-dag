# Audit

- The family is on the generic rank-three side: its pair coefficient points
  lie on a nondegenerate conic, not one affine line.
- Distinct fiber values make all cubic fibers, selected pairs, and omitted
  roots disjoint. The finite-extension step supplies a finite splitting
  field; it is not an official-field assertion.
- The functional is defined only after the `3e+1` displayed ambient
  generators are proved independent.
- The exact `F_101`, `e=12` fixture has pair-locator rank three, ambient rank
  37, and product rank 36. Replacing its last fiber pair by `(2,4)` restores
  rank 37, so the checker detects the claimed defect rather than a dimension
  bug.
- The result fences only Schur-square saturation. The official external
  design could impose additional conditions that eliminate this family.
