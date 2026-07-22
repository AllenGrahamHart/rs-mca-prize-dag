# Claim contract

- **Claim:** the quadratic Veronese matrix of the `6e+3` external monic
  locator vectors has rank at most `3e+1`.
- **Scope:** only the official `A=1`, core-one, exceptional-only,
  quotient-distance-three pair-Lagrange chart.
- **Inputs:** the pair partition of the degree-`2e` locator `A`, the
  degree-three canonical locator `B`, and exact degree-`e` active-row
  locators from the external split design.
- **Dependencies:** pair-Lagrange normal form and external split-design
  saturation.
- **Consumer:** `rate_half_band_closure`; also an early rejection gate for
  CR-003 contributor classifiers.
- **Falsifier:** valid pair-Lagrange data and an exact external design whose
  quadratic locator matrix has rank greater than `3e+1`.
- **Nonclaims:** the rank gate does not classify the low-rank block family,
  prove the resultant-power identity, or exclude the official chart.
