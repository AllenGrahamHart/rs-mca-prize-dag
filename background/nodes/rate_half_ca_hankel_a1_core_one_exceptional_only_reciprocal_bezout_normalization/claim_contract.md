# Claim contract

- **claim id:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_reciprocal_bezout_normalization`
- **mathematical statement:** the first reciprocal coefficient and the next
  `A_1` coefficient form an exact Bezout pair for `P_cl` and `E q_bar`
- **scope:** only the `b=0,D_*=1,c=z=1` corrected square
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **proved dependency:** exceptional-only reciprocal-resultant descent
- **new open content:** use the modular inverse normalization with the Hankel
  adjugate and lower coefficient chain to classify the corrected square
- **falsifier:** a valid corrected square violating `(RBN2)`
- **nonclaims:** no uniqueness of a polynomial representative without an
  additional degree normalization, no lower-coefficient classification, no
  profile exclusion, and no promotion of `rate_half_band_closure`
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_reciprocal_bezout_normalization/verify.py`
- **upstream mapping:** exact SPI / split-pencil leading Bezout ledger
