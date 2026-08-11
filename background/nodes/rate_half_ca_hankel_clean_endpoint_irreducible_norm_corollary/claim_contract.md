# Claim contract

- **Claim:** on the `O=0`, `m>1` failure branch, `Q` is absolutely
  irreducible, the norm defect is linear, and exactly one domain fibre has
  deficit one.
- **Dependencies:** endpoint saturation, norm factorization, and component
  defect localization.
- **Output:** the clean irreducible cyclic-norm profile `(CIN1)--(CIN5)`.
- **Consumer:** the clean branch of `rate_half_band_crossing_location`.
- **Nonclaims:** no exclusion of the dominant irreducible curve and no
  statement for positive omission budget.
- **Falsifier:** a residual algebraic component at `O=0`, more than one
  deficient column, a norm defect of degree other than one, or failure of
  the specialized complementary identity.
- **Replay:** `tools/ramguard tiny -- python3
  background/nodes/rate_half_ca_hankel_clean_endpoint_irreducible_norm_corollary/verify.py`
  and `verify_audit.py`.
