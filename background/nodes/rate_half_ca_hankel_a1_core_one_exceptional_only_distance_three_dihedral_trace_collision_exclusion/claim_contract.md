# Claim contract

- **Claim:** calibrated trace collisions and saturated external incidence
  exclude both dihedral distance-three branches for `e>=31`.
- **Scope:** the nonexceptional pair-complement family after the proved
  dihedral boundary reduction.
- **Dependencies:** pair-complement quadratic trace and external split-design
  saturation.
- **Consumer:** `rate_half_band_closure`.
- **Load-bearing hypotheses:** `P_Z` is squarefree with `3e` external roots;
  every complement has `e` roots; there are at least `3e-3` distinct
  complements; each external block has `2e+1` rows; `mu_i` and `chi(u)` are
  nonzero.
- **Falsifier:** an external root contained in fewer than `e-4` complements,
  a quadratic class larger than `e`, two distinct quadratic classes
  co-selected at more than two orbit coordinates, or a valid packet at
  `e>=31`.
- **Nonclaim:** no assertion is made for `e<=30` or for rate-half branches
  outside this dihedral distance-three chart.
