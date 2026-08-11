# Claim contract

- **Claim:** the canonical reciprocal Padé numerator has bidegree at most
  `(rho-1,m+1)`, its formal resultant with `q` is exactly
  `constant*a^(2rho+2)Delta`, and the good supported specializations give
  the printed Vandermonde-times-Forney product.
- **Dependencies:** the marked adjugate factorization and the full Hankel
  kernel recurrence.
- **Output:** a degree-`m-1` normalized resultant target.
- **Consumer:** the clean branch of `rate_half_band_crossing_location`.
- **Nonclaim:** no bound or noninterpolation theorem for the Forney products.
- **Falsifier:** an incorrect numerator reconstruction, a missing power of
  `a`, disagreement with the top adjugate scalar, or a generic supported
  weight violating `P(x)=theta_x q'(x)`.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_clean_endpoint_forney_resultant_regular_factor/verify.py`
  and `verify_audit.py`.
