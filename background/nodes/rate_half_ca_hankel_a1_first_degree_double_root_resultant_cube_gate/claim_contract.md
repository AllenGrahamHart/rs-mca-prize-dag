# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_double_root_resultant_cube_gate`
- **mathematical statement:** the finite-total-quotient-algebra norm of either
  retained double-root cube identity is the exact resultant quotient
  `(RCG3)`, which must be a cube in `F(z)`; `(RCG6)` gives the
  characteristic-three test
- **scope:** first-degree core-free cubic double-root and core-one quadratic
  double-root scalar branches
- **dependency:** double-root radical cube bridge
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a missing leading-coefficient factor, a wrong norm exponent,
  or a retained packet whose computed `Xi_P` is not a rational cube
- **nonclaims:** the norm-cube condition is not sufficient for a cube in
  `K_C` or for recurrence realization; irreducibility of `C` is not assumed
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_double_root_resultant_cube_gate/verify.py`
- **upstream mapping:** primitive shift-pair control / exact scalar
  resultant ledger
