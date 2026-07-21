# Audit

- `N_c` counts only internally signed-distinct ordered presentations. Some
  nonnode points of the rational cubic have repeated roots; they are omitted,
  so the proof does not falsely assign six presentations to them.
- The subtraction is `6N_c`, not `N_c`: an orbit has six presentations, and
  every ordered pair inside one orbit is forbidden by signed disjointness.
- The quotient-line factor remains target-dependent in the actual count.
  Replacing it by `(51/16)n^(2/3)` is a valid upper bound, not a
  decorrelation assertion.
- `S` is a cubic character sum over the already filtered eligible nodal
  points. A bound for an unfiltered affine intersection would not imply
  `(NTE7)` without an additional argument.
- Sparse classes can have `|S|/N=1`; no uniform `4/5` bias theorem is claimed.
- Such sparse full bias is harmless below `(NTE6a)`. Cubic balance should be
  studied only after a row certifies the narrow high-point interval
  `(NTE6b)`.
- Even when `(NTE7)` holds, the printed `>103n^2` remainder is only a budget
  for the still-open smooth slice. It is not itself a smooth-trace estimate.
