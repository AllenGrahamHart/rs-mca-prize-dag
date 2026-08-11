# Claim contract

- **Claim:** the sole strict corner has an integral endpoint curve, an
  effective degree-one contact bundle, and the univariate identity `(FCP5)`.
- **Dependencies:** the universal contact theorem and single-corner slope
  reduction.
- **Output:** one integral Picard point and one exact divisor identity.
- **Consumer:** `rate_half_band_crossing_location`.
- **Nonclaim:** neither `O=0` nor `O=1` is excluded.
- **Falsifier:** pole length above one, failure of univariate restriction
  descent, a component on which `A_d` vanishes identically, a nonnegative
  degree-zero component solution to `(7)`, or a non-Cartier degree-one zero.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_strict_a3_final_corner_integral_picard_pin/verify.py`
  and `verify_audit.py`.
