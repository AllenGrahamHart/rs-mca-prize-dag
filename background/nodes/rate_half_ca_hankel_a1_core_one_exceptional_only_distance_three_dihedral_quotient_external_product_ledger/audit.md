# Audit

- Fixed active points and crossing orbits belong to `C_1`; neither is
  accidentally assigned exponent `2e` in `(QEP3)`.
- Root multiplicity two records two distinct active rows in one block, not a
  repeated root of the squarefree source locator.
- At a common nonzero external slope, a nonexceptional row difference forces
  `J(z;u)=0`; substituting back gives the nonzero value `Phi(z)E(u)`. Merely
  counting roots of the difference would miss this contradiction.
- The exceptional row pair has codegree exactly `e`, not just at most `e`,
  because its normalized row polynomials are identical.
- The verifier uses the six vertex-stars of `K_6` as a complete
  `e=2,v=15,b=6,k=5` biregular design, checks the polynomial product with
  disjoint paired-row incidence, and independently checks both branch
  difference identities.
