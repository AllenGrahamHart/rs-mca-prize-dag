# Audit

- The partial-fraction coefficients are legal because every removed domain
  point is a simple root and `R_i'(a)!=0`.
- Independence uses the total number of removed points, not the number of
  locator polynomials. The official bound is the exact maximum `C=8`.
- Removed-point sets must be disjoint. Two supported blocks have total size at
  least `2d-4>d` for `d>=8`, so disjoint blocks cannot complete to the same
  `d`-point quotient fiber. Distinct fibers of `x |-> x^d` are disjoint.
- The path relation omits the degree-`d` locator `A_2`; its supported deficit
  total is three, not four.
- The result excludes one quotient-periodic route, not all quotient-periodic
  unions and not a whole incidence chamber.
