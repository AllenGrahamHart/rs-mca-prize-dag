# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_first_degree_double_root_low_degree_resultant_factorization`
- **mathematical statement:** the full `X`-resultant in each retained
  double-root packet factors exactly as the supported locator to the generic
  `X`-degree times a cube of degree one or two, with the printed ordinary
  slope correction
- **scope:** core-free cubic double-root gap-one packets and the core-one
  quadratic double-root packet at `u=4`
- **dependencies:** resultant cube gate and the exact Picard normal forms
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** a leftover leading-coefficient factor, a different
  supported-slope exponent, a residual cube root of degree above two, or a
  failed total-degree identity
- **nonclaims:** satisfying the factorization does not construct the curve,
  recurrence, or packet
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_first_degree_double_root_low_degree_resultant_factorization/verify.py`
- **upstream mapping:** primitive shift-pair control / exact scalar
  resultant ledger
