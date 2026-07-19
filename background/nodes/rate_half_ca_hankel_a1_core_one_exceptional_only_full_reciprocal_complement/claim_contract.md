# Claim contract

- **claim id:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_full_reciprocal_complement`
- **mathematical statement:** after removing the forced infinity
  coefficients, the entire corrected complement is `FU+P_clL=R_X`
- **scope:** only the `b=0,D_*=1,c=z=1` corrected square
- **consumer:** `rate_half_band_closure`
- **status:** `PROVED`
- **proved dependency:** exceptional-only reciprocal Bezout normalization
- **new open content:** combine the divisibility/interpolation form with
  reconstruction of `G`, the unit equation, Hankel adjugate, and splitting
- **falsifier:** a valid corrected square violating `(FRC3)` or `(FRC4)`
- **nonclaims:** no converse from `F,U,L` to the original biforms, no
  automatic divisibility by `E`, no unit or Hankel reconstruction, no
  profile exclusion, and no promotion of `rate_half_band_closure`
- **replay:**
  `tools/ramguard tiny -- python3 background/nodes/rate_half_ca_hankel_a1_core_one_exceptional_only_full_reciprocal_complement/verify.py`
- **upstream mapping:** exact SPI / split-pencil reciprocal complement ledger
