# Claim contract

- **Claim:** if every quartic support crossing is deficient on the official
  generic saturated packet, then either every pair obeys the exact smooth
  antiweight identity or at least `e-148` pairs are fibers of one
  base-field rational map of degree two, three, or four.
- **Scope:** the official prime-field `A=1`, core-one, exceptional-only,
  quotient-distance-three chart after the support pair-crossing gate.
- **Dependencies:** support pair-crossing rank gate and official prime-field
  collapse.
- **Consumer:** `rate_half_band_closure` and the support stage of
  `CR-003-CLIFT`.
- **Falsifier:** an all-deficient official packet which violates global
  antiweight and for which no degree-`2`, `3`, or `4` map contains the
  asserted number of matched fibers.
- **Nonclaims:** neither alternative is excluded here; a low-degree fiber
  packet is not asserted to lift through `U`, `T`, or the external design.
- **Verification:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_support_low_degree_fiber_reduction/verify.py`
