# Claim contract

- **Claim:** the official prime-field shape-A normalization has the exact
  printed Euler-characteristic and genus floors.
- **Dependencies:** the exact classified-row splitting, absolute
  irreducibility and one pure split fiber, and the already audited
  Corvaja--Zannier positive-characteristic gcd theorem.
- **Currency:** distinct normalization points with both coordinates in the
  official multiplicative subgroup.
- **Output:** a necessary high-genus condition for shape A.
- **Consumer:** the shape-A branch of `rate_half_band_crossing_location`.
- **Nonclaims:** shape-A exclusion, a source-derived genus upper bound, or
  extension-field transport.
- **Falsifier:** duplicate or singular counted row points, a translated
  subtorus compatible with the pure split fiber, failure of the strict
  characteristic branch, or an arithmetic mismatch in `(SGF4)--(SGF5)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_shape_a_global_subgroup_genus_floor/verify.py
  --tamper-selftest`.
