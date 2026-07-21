# Claim contract

- **claim:** every complete one-antipodal `c=2` packet either has distinct
  barycentric weights and support at least `4H-2`, or has exactly one weight
  collision and lies on the printed `L/Q` branches with the square-class
  gate.
- **scope:** all complete canonical one-antipodal packets at the maximal
  rate-half row, not only minimum-support packets.
- **dependencies:** canonical cells, the pointwise support compiler,
  normalized outer/coupling equations, and the torsion-field square lift.
- **consumer:** `rate_half_list_adjacent_crossing`.
- **falsifier:** a covered packet with distinct weights and support below
  `4H-2`, or a collision packet outside `(CHR3)--(CHR7)`.
- **nonclaims:** neither branch is excluded, and the minimum-support Euler,
  endpoint, infinity, and affine gates are not extended to larger support.
