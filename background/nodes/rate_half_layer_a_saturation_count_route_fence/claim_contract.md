# Claim contract

- **Claim:** at `m=2`, `rho=7`, `T=9`, and `a=13`, there is an exact
  pointwise-saturated Layer-A incidence system with 26 rows and 24 columns
  whose evaluation matrix has rank 20 and nullity four.
- **Dependencies:** none beyond elementary finite-field and polynomial-root
  facts proved in the packet.
- **Output:** `(LAW1)`--`(LAW3)` and a route fence against promoting the
  count `3m^2-5m>0` to a rank theorem.
- **Consumer:** the Layer-A route inside
  `rate_half_band_crossing_location`.
- **Nonclaims:** no full endpoint-pencil witness, no canonical pair-union
  support, no global support completion, and no counterexample to a theorem
  using the Hankel/source or split-biform constraints.
- **Falsifier:** failure of primitive-order, saturation, matrix-rank, kernel,
  or nonzero-minor checks in either exact replay.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_layer_a_saturation_count_route_fence/verify.py`
  and the independent fixed-minor audit `verify_audit.py`.
