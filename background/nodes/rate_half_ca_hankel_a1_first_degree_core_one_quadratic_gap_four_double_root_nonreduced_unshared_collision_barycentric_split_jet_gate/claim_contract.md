# Claim contract

- **Claim:** the nonreduced collision is an unsupported parameter and its
  value and derivative jets are four explicit barycentric functionals of
  the unique classified-row weld vector.
- **Dependencies:** collision Pade/split-jet dictionary, all-excess vertical
  fiber gcd, and connected scalar-weld rank dichotomy.
- **Output:** `(BSJ2)`, `(BSJ4)`, `(BSJ6)`, and `(BSJ7)`.
- **Consumer:** the unshared nonreduced arm of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no rank or nonvanishing assertion beyond the exact
  collision conditions.
- **Falsifier:** a supported unshared collision, a failed derivative
  interpolation formula, or a profile not selected by `J_0,J_1`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_barycentric_split_jet_gate/verify.py`.
