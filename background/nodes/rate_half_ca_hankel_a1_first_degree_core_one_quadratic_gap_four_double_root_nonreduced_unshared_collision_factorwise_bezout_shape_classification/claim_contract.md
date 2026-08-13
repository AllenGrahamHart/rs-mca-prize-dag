# Claim contract

- **Claim:** in the surviving `d_A=1` nonreduced collision, factorwise
  Bezout capacity and local contact length restrict `G` to the four shapes
  A--D in `(FBS7)`.
- **Dependencies:** the exact factor trichotomy and profile-I reduction,
  all-excess transverse fiber factorization, exact four-core, center-adjusted
  heavy row, and exact collision contact router.
- **Output:** `(FBS4)--(FBS7)`; the large factor has degree at least `e-6`
  and ordinary companions total at most four.
- **Consumer:** the unshared nonreduced arm of
  `rate_half_band_crossing_location`.
- **Nonclaims:** no shape is excluded and no factor is asserted to exist.
- **Falsifier:** a valid collision factorization with residual factorwise
  intersection not exhausted by padding and collision, local length not
  equal to twice correction order, or an ordinary factor outside the two
  records in `(13)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_factorwise_bezout_shape_classification/verify.py`.
