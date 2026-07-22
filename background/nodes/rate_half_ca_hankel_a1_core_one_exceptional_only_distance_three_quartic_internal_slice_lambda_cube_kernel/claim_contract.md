# Claim contract

- **Claim:** evaluating the quartic boundary at each internal slope gives a
  theta-free degree-four remainder condition, linear in the cube vector
  `(lambda_i^3)`. A valid design supplies a full-support kernel vector for
  the explicit matrix `U`.
- **Scope:** the official `e>=4` generic saturated distance-three chart.
- **Dependency:** quartic boundary torus-kernel reduction.
- **Consumer:** `rate_half_band_closure` and `CR-003-CLIFT`; earliest exact
  support/pair/internal-slope rejection gate.
- **Falsifier:** a valid exact design violating `(QLK2)--(QLK8)`, or a
  claimed full-rank/coloop certificate with a full-support kernel vector.
- **Nonclaims:** no universal rank theorem, no assertion that every
  deletion-stable torus vector is coordinatewise cubic, and no external
  split-design nonexistence result.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_internal_slice_lambda_cube_kernel/verify.py`
