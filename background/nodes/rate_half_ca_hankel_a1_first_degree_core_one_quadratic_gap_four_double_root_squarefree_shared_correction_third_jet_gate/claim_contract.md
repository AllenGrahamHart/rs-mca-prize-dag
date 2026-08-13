# Claim contract

- **Claim:** at a simple root shared by `g_*` and `S_B`, one explicit
  coefficient `kappa_tau` is exactly the obstruction to `D_1`-divisibility
  of the canonical divided-heavy-row moments.
- **Dependencies:** double-root vertical/contact divisors, the exact
  `Q(t,x_*)` and `D_1` factors, the contracted Pade identity, and the Hankel
  kernel recurrence.
- **Output:** `(HSJ3)--(HSJ6)` and Smith type `[3]` on the vanishing branch.
- **Consumer:** the squarefree shared-root route in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no decision of the jet sign and no nonreduced-root claim.
- **Falsifier:** a shared squarefree packet violating order-two divisibility,
  recurrence propagation, or the equivalence in `(HSJ6)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_squarefree_shared_correction_third_jet_gate/verify.py`
  and `verify_audit.py`.
