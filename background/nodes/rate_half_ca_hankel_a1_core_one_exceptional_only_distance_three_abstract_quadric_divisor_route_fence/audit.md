# Audit

- The construction uses three swap pencils, not arbitrary points fitted to a
  quadric after the fact.
- Distinctness includes the common pencil vertex exactly once.
- The direction conic has rank three because its scaled symmetric matrix has
  determinant two; odd characteristic is load-bearing.
- The verifier checks `e=4` over `F_97`: all 25 classes divide one squarefree
  degree-12 polynomial, span the printed four-space, lie on the cone, and
  exceed the target count nine.
- This fence invalidates only an abstract quadric-count route. The exact
  `mu_i,chi(u),u_i` interpolation data remain untested by the construction.
