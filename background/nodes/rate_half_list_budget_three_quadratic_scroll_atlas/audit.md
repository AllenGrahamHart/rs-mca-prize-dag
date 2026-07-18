# Audit

- The balancing row operation uses `b_03`, which is tight and exactly linear
  in all four quadratic chambers.
- A quadratic `b_13` occurs only in the pendant type, where `b_02` is
  constant; therefore balancing coordinate three cannot create a quadratic
  term in coordinate two.
- Row addition preserves every Plucker minor and transforms the locator
  coefficients exactly as in `(QSA4)`.
- `b_01` is a nonzero constant, so `alpha,beta` remain polynomials over the
  base field.
- Genuine degree two is pinned by `U_1 wedge V_1!=0`, not inferred merely
  from the word "quadratic".
- In the rank-deficient subbranch, relation support has size at least three;
  no assertion is made that all four coefficients are nonzero.
- Exceptional degrees count selected domain coordinates: four pendant edge
  points, or five `K_4-e` edge points plus one full point.
- The normal form completes bounded edge geometry but does not solve the
  resulting subgroup factorization.
