# Claim contract

- **claim id:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_factor_pin`
- **mathematical statement:** the unique middle-Hankel regular factor is the
  exceptional form `E` up to scalar, and the divided exceptional cofactor
  matrix is a nonzero rank-one outer product
- **scope:** only the official `b=0,D_*=1,c=z=1` corrected square
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **proved dependencies:** middle-adjugate factorization and the full
  exceptional-only reciprocal square chain
- **new open content:** impose the pinned cofactor products together with the
  reciprocal triangular reconstruction, degree boxes, and split fibers
- **falsifier:** a valid exceptional-only packet with the middle-Hankel
  regular factor not associated to `E`, or with `(HFP3)` zero or non-rank-one
- **nonclaims:** no normalization of `c_H` by a square root, no assertion that
  `E` does not divide `q_bar`, no stronger `E`-adic valuation than `(HFP5)`,
  no profile exclusion, and no promotion of `rate_half_band_closure`
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_factor_pin/verify.py`
- **upstream mapping:** base-field-normalized exact SPI middle-Hankel cofactor
  ledger
