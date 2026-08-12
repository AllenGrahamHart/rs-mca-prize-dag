# Claim contract

- **Claim:** every shape-C `(4,6)` companion has a deck involution acting as
  `X -> -X` or `X -> k/X`, and descends to a `(4,3)` quotient biform.
- **Dependencies:** the A/C shape reduction, exact factorwise saturation,
  and the audited Corvaja--Zannier theorem.
- **Output:** two explicit involution arms replacing an arbitrary quartic
  companion.
- **Consumer:** shape C inside `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of either involution, no exclusion of shape C,
  and no statement about shape A.
- **Falsifier:** a valid shape-C companion with no toral off-diagonal
  component, or a toral component not inducing one of the two involutions.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_ordinary_quartic_companion_toral_deck_involution_router/verify.py`.
