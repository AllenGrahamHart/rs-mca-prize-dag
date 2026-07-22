# Claim contract

- **Claim:** every official static Pade class leaves a nonconstant residual
  pencil of degree at most four, aligned at at least `e-33` or `e-44` orbit
  coordinates, with each outside external root used at most twice.
- **Scope:** the single all-deficient support leaf after pullback absorption.
- **Dependencies:** static-denominator reduction and the exact external split
  design.
- **Consumer:** `rate_half_band_closure`; replaces the high-degree gcd target
  by a four-case low-degree split-pencil classification.
- **Falsifier:** an aligned complement missing one class root, an outside
  root occurring at three aligned coordinates, residual degree at least
  five, or fewer aligned coordinates than `(QPAR1)`.
- **Nonclaims:** the remaining degree-1-to-4 pencils are not excluded here.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_pade_aligned_residual_degree_four/verify.py`
