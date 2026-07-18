# Claim contract

- **Claim:** the official dominant strict-endpoint component of bidegree
  `(4e-1,e)` is not an irreducible separated fiber product `f(X)=g(U:V)` of
  rational maps of degrees `4e-1` and `e`; equivalently, its separation rank
  is at least three.  The full primitive generator also has separation rank
  at least three.
- **Scope:** only the first strict `A=3` endpoint with `m=2^37`; the exact
  component profile and column-defect budget are required.
- **Dependency:**
  `rate_half_ca_hankel_endpoint_component_defect_localization` supplies
  `ceil((3m+1)/4)<=e<=m` and `C_*<=m`.
- **Consumer:** the strict `e=m`, `A=3` branch of
  `rate_half_band_closure`.
- **Nonclaims:** arbitrary mixed biforms remain possible; no classification
  of rational-map fiber products with smaller component bidegree is asserted;
  no other endpoint parameter degree is covered.
- **Next exact gate:** exploit the Hankel/apolar coefficient chain against a
  separation-rank-at-least-three dominant biform with the already-proved
  split-fiber and low-defect properties.
