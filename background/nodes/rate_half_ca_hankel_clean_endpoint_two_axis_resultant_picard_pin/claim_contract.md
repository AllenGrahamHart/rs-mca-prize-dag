# Claim contract

- **Claim:** after a harmless generic domain-coordinate normalization, the
  reciprocal resultants are `(TAP3)` and the saturated `B` divisor yields
  `O_C(N,-T)=O_C(P_*)` of degree one.
- **Dependency:**
  `rate_half_ca_hankel_clean_endpoint_resultant_boundary_saturation`.
- **Output:** the exact two-axis resultant square and degree-one Picard pin.
- **Consumer:** the clean branch of `rate_half_band_crossing_location`.
- **Nonclaim:** degree one does not by itself imply a degree-one map or
  rationality of a singular integral curve.
- **Falsifier:** an unaccounted projective intersection, a factor of `a` in
  `Res_X(Q,B)`, an `X`-resultant factor outside `(TAP3)`, or a divisor degree
  other than one.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_clean_endpoint_two_axis_resultant_picard_pin/verify.py`
  and `verify_audit.py`.
