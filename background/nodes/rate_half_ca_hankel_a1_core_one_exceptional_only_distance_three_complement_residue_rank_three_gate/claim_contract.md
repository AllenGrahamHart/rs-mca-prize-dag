# Claim contract

- **Claim:** the degree-`2e` external complement locators `P_Z/G_x`, reduced
  modulo the internal locator `I`, span a space of dimension at most three;
  their full polynomial coefficient span has dimension at most `e+4`.
- **Scope:** only the official `A=1`, core-one, exceptional-only,
  quotient-distance-three pair-Lagrange chart.
- **Inputs:** the pair-Lagrange internal slopes and pair fibers, plus the
  exact external split design.
- **Dependencies:** pair-Lagrange normal form, external split-design
  saturation, and the pair-locator Mobius dichotomy.
- **Consumer:** `rate_half_band_closure`; preferred early filter for CR-003
  external block packets.
- **Falsifier:** a valid pair-Lagrange external design for which either the
  inverse-locator or complement-residue matrix has rank at least four, or
  whose full complement coefficient matrix has rank greater than `e+4`.
- **Nonclaims:** no classification or exclusion of rank-three residue
  families is asserted.
