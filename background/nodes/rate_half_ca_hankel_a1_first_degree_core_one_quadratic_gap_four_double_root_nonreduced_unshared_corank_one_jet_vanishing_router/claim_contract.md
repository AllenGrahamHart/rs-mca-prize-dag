# Claim contract

- **Claim:** both unshared nonreduced Hasse jets vanish whenever the regular
  specialization has corank one and the compressed minimal recurrence is
  nonzero at `x_*`; a nonzero corank-one jet routes to that recurrence-root
  collision.
- **Dependencies:** the exact nonreduced unshared two-jet gate and symmetry
  of the regular Hankel block.
- **Output:** `(HCR2)--(HCR4)`.
- **Consumer:** the nonreduced double-root branch in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no automatic separation from `x_* notin U_0`, no proof that
  every nonreduced correction has regular corank one, and no shared-root
  claim.
- **Falsifier:** a separated contracted-source corank-one order-four block
  with either obstruction jet nonzero.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_corank_one_jet_vanishing_router/verify.py`
  and `verify_audit.py`.
