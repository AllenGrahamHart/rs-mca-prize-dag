# Claim contract

- **Claim:** both unshared nonreduced Hasse jets vanish whenever the regular
  specialization has corank one; a nonzero jet routes to higher corank.
- **Dependencies:** the exact nonreduced unshared two-jet gate and symmetry
  of the regular Hankel block.
- **Output:** `(HCR2)--(HCR4)`.
- **Consumer:** the nonreduced double-root branch in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no proof that every nonreduced correction has regular
  corank one and no shared-root claim.
- **Falsifier:** an actual contracted-source corank-one order-four block with
  either obstruction jet nonzero or with `P_tau(x_*)=0` despite
  `x_* notin U_0`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_corank_one_jet_vanishing_router/verify.py`
  and `verify_audit.py`.
