# Audit

- `O=0` is used termwise, so every supported residual locator has exactly
  `d` distinct residual domain roots; this is stronger than an average.
- The fixed core point is added once to every residual locator.
- `I_H` counts all distinct supported incidences on heavy rows. Since the
  double root carries all of it, the other `rho-7` heavy rows are inactive.
- Nearest codewords are unique because `2rho<d_min=2rho+1`.
- Error supports may be strict subsets of the padded locator blocks; this is
  sufficient for the triple-union argument.
- At a deficient slope, `x_*` is a simple new excess root, so it is padding
  rather than an actual error location. This gives exact error weight
  `rho-1`; all other supported slopes have weight `rho`.
- The line cap uses column-farness of the pair, not merely individual
  distance at the supported slopes.
- The theorem does not assume positivity or a balanced block design.
