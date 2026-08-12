# Claim contract

- **Claim:** exact normalization valuations force every unshared
  nonreduced correction either to close at `ord_tau F_0=4` or to have
  `ord_tau F_0=2`, `kappa_2!=0`, and an exact double quotient-root collision.
- **Dependencies:** the minimum-gap root/contact divisors, two-jet gate, and
  higher-corank locator router.
- **Output:** `(NCD3)--(NCD5)`, including elimination of every first-nonzero
  third-jet and every noncollision nonzero-jet profile.
- **Consumer:** the nonreduced double-root branch in
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion or Smith classification of the exact collision;
  no shared-nonreduced assertion.
- **Falsifier:** a correction point violating `e_b s=2m_b`, a first-nonzero
  third jet, or a nonzero second jet without specialized root multiplicity
  exactly two.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_normalization_collision_dichotomy/verify.py`
  and `verify_audit.py`.
