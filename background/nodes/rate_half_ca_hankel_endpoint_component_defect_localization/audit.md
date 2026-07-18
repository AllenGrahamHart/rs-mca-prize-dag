# Audit

- `E` is overlap of distinct component incidence sets, not root
  multiplicity.  Geometric squarefreeness is proved first, so the component
  list has no repeated factors.
- The exact sums use distinct grid zeros.  Component overlap increases
  `sum I_i` and therefore subtracts the same `E` from both defect ledgers.
- A generic-rank supported slope has `rho` distinct domain roots.  Equality
  of total degrees prevents any component degree drop there, so every
  component is individually split and component root sets are disjoint.
- A saturated domain column has `m` distinct parameter roots.  Every
  component specialization is nonzero of its full homogeneous parameter
  degree, so the analogous column conclusion is exact.
- The factor-four residual charge is arithmetic, not an asymptotic estimate:
  `T*(4e_i)-N*e_i=4e_i` for each balanced component.
- The verifier checks the ledgers for small omission/overlap profiles,
  official constants, and DAG wiring.  It does not test the open nonlinear
  cover classification.
