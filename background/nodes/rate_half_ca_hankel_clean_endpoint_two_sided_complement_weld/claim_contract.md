# Claim contract

- **Claim:** every clean strict-endpoint failure admits the dual complement
  `(CWD2)` and the two-sided weld `(CWD5)--(CWD8)` with the printed degrees.
- **Dependency:**
  `rate_half_ca_hankel_clean_endpoint_irreducible_norm_corollary`.
- **Output:** a nonzero factor `B` of parameter degree at most `m-1` whose
  product with `W` is `X-x_0` in the irreducible curve function field.
- **Consumer:** the clean branch of `rate_half_band_crossing_location`.
- **Nonclaim:** the weld alone does not exclude the curve or prove either
  factor constant.
- **Falsifier:** a clean profile for which a supported quotient fails to
  interpolate to `(CWD2)`, coprimality fails, or either weld identity or
  degree bound is false.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_clean_endpoint_two_sided_complement_weld/verify.py`
  and `verify_audit.py`.
