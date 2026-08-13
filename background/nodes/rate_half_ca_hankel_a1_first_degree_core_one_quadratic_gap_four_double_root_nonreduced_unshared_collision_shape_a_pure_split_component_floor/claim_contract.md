# Claim contract

- **Claim:** shape A has at least `e+7` pure split fibers, forcing one
  off-diagonal component to contain at least `n+14` subgroup points.
- **Dependencies:** shape-A norm concentration, all-excess fiber
  factorization, and primitive factor classification.
- **Output:** an absolute-irreducibility proof and exact component point floor.
- **Consumer:** shape A inside `rate_half_band_crossing_location`.
- **Nonclaims:** no translated-subtorus conclusion and no shape-A exclusion.
- **Falsifier:** fewer than `e+7` pure fibers, geometric reducibility of the
  large factor, or a component partition whose total misses the pair floor.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_shape_a_pure_split_component_floor/verify.py`.
