# Claim contract

- **Claim:** the two coefficients routing the exact collision are the first
  two coefficients of the second divided-row moment and, equivalently, the
  first two parameter jets of `G_X(t,x_*)`.
- **Dependencies:** exact-collision Smith router, Pade regular-factor
  identity, and the extremal three-center source partition.
- **Output:** `(PSD5)--(PSD10)`.
- **Consumer:** the unshared nonreduced arm of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of `[4]`, `[1,3]`, or `[2,2]`; no shared-root
  or characteristic-two assertion.
- **Falsifier:** a mismatch among the Pade remainder, second divided-row
  moment, derivative pairing, and split-biform jets.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_pade_split_jet_dictionary/verify.py`.
