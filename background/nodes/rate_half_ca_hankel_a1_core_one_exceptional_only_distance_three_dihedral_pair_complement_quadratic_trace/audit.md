# Audit

- The exceptional identical-row orbit is omitted from `(PCT1)` because its
  squared row polynomial does not divide squarefree `P_Z`.
- Raw row polynomials need not be monic. Their nonzero leading scalars are
  absorbed into `a_u` and `chi(u)`; projective divisor classes are unchanged.
- The interpolation includes the degree-`e` term `a_uI`. Dropping it would
  incorrectly claim that all complements lie in a three-dimensional vector
  space.
- Injectivity uses `e>=3`, which holds by a vast margin on the official row.
- The verifier checks exact interpolation, four-dimensionality, the cone
  equation, and projective distinctness over `F_97`. The official divisor
  property itself follows from the proved disjoint row-root sets.
