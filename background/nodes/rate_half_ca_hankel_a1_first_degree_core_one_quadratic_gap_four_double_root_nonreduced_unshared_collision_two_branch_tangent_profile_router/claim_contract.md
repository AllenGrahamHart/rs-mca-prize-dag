# Claim contract

- **Claim:** collision shapes B and D cannot realize profile `[4]`; their
  remaining profile is `[1,3]` or `[2,2]` according as the tangent sum
  `Theta` is nonzero or zero.
- **Dependencies:** factorwise four-shape classification and the exact
  Pade/split-jet profile dictionary.
- **Output:** one scalar tangent-cancellation gate for each two-branch shape.
- **Consumer:** the unshared nonreduced collision arm of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of B or D, no nonvanishing claim for `Theta`,
  and no profile restriction for A or C.
- **Falsifier:** a valid shape B or D with `G_X(tau,x_*)!=0`, or one whose
  first parameter coefficient of `G_X` differs from a nonzero unit times
  `a_1v_2+a_2v_1`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_two_branch_tangent_profile_router/verify.py`.
