# Claim contract

- **Claim:** the residual pair mass after deleting the known quartic deck
  graph forces a second deck involution, which is group-theoretically
  impossible; hence only shape A remains.
- **Dependencies:** the four-shape classification, quadratic-companion
  exclusion, quartic deck-involution router, and audited
  Corvaja--Zannier theorem.
- **Output:** unconditional deletion of shapes B, C, and D.
- **Consumer:** the unshared nonreduced branch of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of shape A and no closure of the parent
  crossing node.
- **Falsifier:** a residual pair census below `6F_6`, a fifth residual
  component, or two distinct subgroup-compatible involutions in a
  degree-six deck group without an order-four subgroup.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_ordinary_companion_complete_shape_exclusion/verify.py`.
