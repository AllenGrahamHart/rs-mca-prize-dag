# Claim contract

- **Claim:** both unshared nonreduced Hasse jets vanish on the simple
  corank-one regular locus; a nonzero jet routes to higher corank or a
  collision with the specialized minimal locator.
- **Dependencies:** the exact nonreduced unshared two-jet gate and symmetry
  of the regular Hankel block.
- **Output:** `(HCR2),(HCR3)`.
- **Consumer:** the nonreduced double-root branch in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no proof that every nonreduced correction has regular
  corank one or that `U_tau(x_*)` is always nonzero; no shared-root claim.
- **Falsifier:** a symmetric corank-one order-four block satisfying
  `(HCR1)` with either obstruction jet nonzero.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_corank_one_jet_vanishing_router/verify.py`
  and `verify_audit.py`.
