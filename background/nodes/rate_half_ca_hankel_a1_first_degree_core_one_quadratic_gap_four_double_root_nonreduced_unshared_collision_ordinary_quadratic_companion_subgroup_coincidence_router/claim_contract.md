# Claim contract

- **Claim:** every dense off-diagonal coincidence component of a
  bidegree-`(2,3)` collision companion fails all swap/inversion coordinate
  normalizations needed by the published subgroup-curve estimate.
- **Dependencies:** factorwise shape classification, factorwise row
  saturation, prime-field collapse, and the audited Vyugin--Makarychev
  estimate.
- **Output:** a finite coordinate-corner exceptional locus, separated into
  `S_3` and cyclic degree-three monodromy arms.
- **Consumer:** the companion-bearing B/D arm of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no classification of the corner-exceptional locus, no
  exclusion of B or D, no result for the `(4,6)` companion, and no
  extension-field theorem.
- **Falsifier:** a VM-admissible dense component satisfying the official
  incidence ledger, or failure of either exact cubed inequality.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_ordinary_quadratic_companion_subgroup_coincidence_router/verify.py`.
