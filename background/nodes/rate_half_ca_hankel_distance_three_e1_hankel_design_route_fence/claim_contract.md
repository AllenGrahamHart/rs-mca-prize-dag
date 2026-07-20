# Claim contract

- **scope:** the explicit `e=1,r=3` rate-half analogue over `F_17`
- **mathematical statement:** the printed syndromes give a column-far affine
  Hankel pencil with exactly the five supported slopes, the exact external
  split design, exceptional transversality, and pinned adjugate
- **consumer:** `rate_half_band_closure` as route evidence only
- **status:** `PROVED`
- **load-bearing checks:** exhaustive `1820`-locator column-far census, all
  `18` projective slopes, exact finite-field ranks, every adjugate entry,
  product identity, and quotient-support enumeration
- **nonclaims:** `r=3` is below the official unique-triple threshold; the
  fixture is not an official row, a prize counterexample, or a certificate
  for the corrected reciprocal square
- **falsifier:** any mismatch in the printed moments, ranks, locators,
  supported slopes, incidence multiplicities, adjugate, or support triples
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_distance_three_e1_hankel_design_route_fence/verify.py`
- **upstream mapping:** exact finite SPI/Hankel low-order route fence
