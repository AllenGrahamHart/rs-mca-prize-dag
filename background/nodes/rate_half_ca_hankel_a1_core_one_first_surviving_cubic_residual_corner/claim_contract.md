# Claim contract

- **claim id:** `rate_half_ca_hankel_a1_core_one_first_surviving_cubic_residual_corner`
- **mathematical statement:** the first surviving official core-one degree
  has only `T=rho+2`, at least `2e+3` clean fibres, and a regular determinant
  whose quotient by the pole divisor has degree at most three
- **scope:** `m=2^37`, `s=1`, `e=floor(16m/13)`
- **dependencies:** the all-degree core-one carrier inequality and the
  general middle-Hankel adjugate-pole factorization
- **consumer:** `rate_half_band_crossing_location`
- **status:** `PROVED`
- **falsifier:** another admissible slack, `p<Delta-3`, fewer than `2e+3`
  clean fibres, or a residual adjugate factor of degree greater than three
- **nonclaims:** the cubic residual is not classified or excluded
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_first_surviving_cubic_residual_corner/verify.py`
- **upstream mapping:** finite exact symmetric-Hankel / SPI ledger
