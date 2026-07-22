# Audit

- The abstract trigonal construction is not contradicted. The exclusion uses
  the official prime field and the fact that every selected root lies in one
  multiplicative subgroup of order `2^41`.
- Cancellation in `B/R` is handled before the curve bound. A reduced
  degree-two map would put every pair under one deck involution and violate
  the rank-three hypothesis.
- The affine hypotheses of the published estimate are not assumed. The
  coefficient array is printed, all ordinary toric corners are classified,
  and the two exceptional boundary forms receive explicit determinant-one
  monomial coordinate changes.
- Absolute irreducibility is split from geometric reducibility. A reducible
  cubic coincidence curve is a cyclic order-three deck pair, not an
  anonymous pair of bidegree-`(1,1)` factors.
- The two subgroup-heavy Mobius graphs are retained and excluded by their
  orders: `x |-> k/x` has order two, while an order-three scaling in a
  `2`-group is the identity.
- The verifier checks the worst bidegree constant, exact integer margins,
  the complete small-field corner classification, both exceptional torus
  transformations, and the general Mobius-graph case split.
